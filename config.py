import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key_student_wallet'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///wallet.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False