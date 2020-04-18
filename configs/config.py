import os
import secrets

class Config():
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Leon@1996@localhost:5432/users'
    DEBUG=True

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
