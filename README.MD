# Ứng Dụng Quản Lý Chi Tiêu Sinh Viên (6 Hũ JARS)

Ứng dụng web hỗ trợ học sinh, sinh viên quản lý tài chính cá nhân hiệu quả dựa trên **Phương pháp 6 hũ tài chính (JARS)** và **Cảnh báo hạn mức chi tiêu**.

##  Tính Năng Chính
- **Cấu hình Hạn mức & Tỷ lệ 6 Hũ**: Tự động phân bổ thu nhập theo 6 hũ (Nhu cầu thiết yếu, Tự do tài chính, Học tập, Hưởng thụ, Tiết kiệm dài hạn, Cho đi).
- **Quản lý Thu / Chi**: Thêm, xóa, phân loại các khoản thu nhập và chi tiêu.
- **Nhập dữ liệu nhanh từ Excel**: Hỗ trợ import lịch sử giao dịch trực tiếp từ file `.xlsx`.
- **Biểu đồ trực quan**: Biểu đồ theo dõi hạn mức tháng và tiến độ số dư/đã chi của từng hũ.

## Công Nghệ Sử Dụng
- **Backend**: Python, Flask, Flask-SQLAlchemy, Pandas, Openpyxl
- **Frontend**: Bootstrap 5, Jinja2, Chart.js
- **Database**: SQLite (`wallet.db`)

## Hướng Dẫn Cài Đặt & Chạy Trực Tiếp Tại Máy (Local)

### 1. Tải dự án về máy
```bash
git clone [https://github.com/toanphanlethanh-svg/Qu-n-l-chi-ti-u-cho-h-c-sinh-sinh-vi-n-.git](https://github.com/toanphanlethanh-svg/Qu-n-l-chi-ti-u-cho-h-c-sinh-sinh-vi-n-.git)
cd Qu-n-l-chi-ti-u-cho-h-c-sinh-sinh-vi-n-