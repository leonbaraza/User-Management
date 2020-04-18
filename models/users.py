from app import db, app
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email_confirmed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    def get_verification_token(self, expires_sec=86400):
        ts = Serializer(app.config['SECRET_KEY'], expires_sec)
        print(self.id)
        return ts.dumps({'user_id' : self.id}).decode('utf-8')

    @staticmethod
    def verify_secret_token(token):
        ts = Serializer(app.config['SECRET_KEY'])
        user_id = ts.loads(token)["user_id"]
        print(user_id)
        print(ts)
        # try:
        #     user_id = ts.loads(token)["user_id"]
        #     print('leon1')
        #     print(user_id)
        # except Exception as e:
        #     return None
        #     print('leon2')
        return UserModel.query.get(user_id)
        

    def  add_user(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first_or_404()


    @classmethod
    def update_user(cls, new_email=None, new_password=None, new_email_confirmed=None):
        user = UserModel.get_user_by_email(new_email)
        
        if user:
            user.email = new_email if new_email else user.email
            user.password = new_password if new_password else user.password
            user.email_confirmed = new_email_confirmed if new_email_confirmed else user.email_confirmed
            
            db.session.commit()