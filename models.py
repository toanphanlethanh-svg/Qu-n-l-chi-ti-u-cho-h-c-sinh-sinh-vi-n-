from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    trans_type = db.Column(db.String(10), nullable=False)  # 'Thu' hoặc 'Chi'
    category = db.Column(db.String(55), nullable=False)
    jar = db.Column(db.String(55), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    note = db.Column(db.String(200), nullable=True)

class JarSetting(db.Model):
    __tablename__ = 'jar_settings'
    id = db.Column(db.Integer, primary_key=True)
    jar_name = db.Column(db.String(55), unique=True, nullable=False)
    percentage = db.Column(db.Float, nullable=False)

DEFAULT_JARS = {
    "Thiết yếu": 55.0,
    "Tiết kiệm": 10.0,
    "Giáo dục": 10.0,
    "Hưởng thụ": 10.0,
    "Đầu tư": 10.0,
    "Cho đi": 5.0
}

def init_default_jars():
    if JarSetting.query.count() == 0:
        for name, pct in DEFAULT_JARS.items():
            db.session.add(JarSetting(jar_name=name, percentage=pct))
        db.session.commit()