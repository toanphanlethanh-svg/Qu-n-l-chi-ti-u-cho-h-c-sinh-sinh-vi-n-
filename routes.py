from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Transaction, JarSetting
from excel_helper import process_excel_import
from datetime import datetime

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    transactions = Transaction.query.order_by(Transaction.id.desc()).all()
    jar_settings = JarSetting.query.all()
    
    # Hạn mức mặc định là 2,000,000 VNĐ
    monthly_budget = float(request.args.get('monthly_budget', 2000000))
    ratios = {j.jar_name: j.percentage / 100.0 for j in jar_settings}

    # 1. Thống kê tổng quan
    total_income = sum(t.amount for t in transactions if t.trans_type == 'Thu')
    total_expense = sum(t.amount for t in transactions if t.trans_type == 'Chi')
    total_savings = total_income - total_expense

    # Kiểm tra vượt hạn mức
    is_over_budget = total_expense > monthly_budget

    # 2. Tính số dư các Hũ
    jars_balance = {name: 0.0 for name in ratios.keys()}
    jars_spent = {name: 0.0 for name in ratios.keys()}
    
    for t in transactions:
        if t.trans_type == 'Thu':
            for name, ratio in ratios.items():
                jars_balance[name] += t.amount * ratio
        elif t.trans_type == 'Chi':
            if t.jar in jars_balance:
                jars_balance[t.jar] -= t.amount
                jars_spent[t.jar] += t.amount

    # 3. Phân tích Chi tiêu theo Danh mục
    category_expenses = {}
    for t in transactions:
        if t.trans_type == 'Chi':
            category_expenses[t.category] = category_expenses.get(t.category, 0) + t.amount

    return render_template('index.html', 
                           transactions=transactions,
                           jar_settings=jar_settings,
                           total_income=total_income,
                           total_expense=total_expense,
                           total_savings=total_savings,
                           jars_balance=jars_balance,
                           jars_spent=jars_spent,
                           category_expenses=category_expenses,
                           monthly_budget=monthly_budget,
                           is_over_budget=is_over_budget)

@main_bp.route('/update-jars', methods=['POST'])
def update_jars():
    jar_settings = JarSetting.query.all()
    total_pct = 0.0
    
    for jar in jar_settings:
        new_val = float(request.form.get(f'jar_{jar.id}', jar.percentage))
        jar.percentage = new_val
        total_pct += new_val

    if round(total_pct, 2) != 100.0:
        flash(f"Tổng tỷ lệ các hũ hiện tại là {total_pct}%. Cần chỉnh về 100%!", "warning")
    else:
        flash("Cập nhật tỷ lệ hũ thành công!", "success")
        
    db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/add', methods=['POST'])
def add_transaction():
    date = request.form.get('date') or datetime.now().strftime('%Y-%m-%d')
    new_trans = Transaction(
        date=date,
        trans_type=request.form.get('trans_type'),
        category=request.form.get('category'),
        jar=request.form.get('jar'),
        amount=float(request.form.get('amount', 0)),
        note=request.form.get('note')
    )
    db.session.add(new_trans)
    db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/import-excel', methods=['POST'])
def import_excel():
    file = request.files.get('file')
    if not file or file.filename == '':
        return redirect(url_for('main.index'))

    try:
        count = process_excel_import(file)
        flash(f"Nhập thành công {count} giao dịch từ Excel!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Lỗi đọc file Excel: {str(e)}", "danger")

    return redirect(url_for('main.index'))