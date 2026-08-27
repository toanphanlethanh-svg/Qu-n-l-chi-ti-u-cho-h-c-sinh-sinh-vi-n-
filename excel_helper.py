import pandas as pd
from models import db, Transaction

def process_excel_import(file):
    df = pd.read_excel(file)
    added_count = 0
    
    for _, row in df.iterrows():
        new_trans = Transaction(
            date=str(row['Ngày']),
            trans_type=str(row['Loại']),
            category=str(row['Danh mục']),
            jar=str(row['Hũ chi tiêu']),
            amount=float(row['Số tiền']),
            note=str(row.get('Ghi chú', ''))
        )
        db.session.add(new_trans)
        added_count += 1
        
    db.session.commit()
    return added_count