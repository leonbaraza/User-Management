from flask import render_template, redirect, url_for
from app import app,db, mail
from utils.security import *
from utils.send_email import send_email
from flask_mail import Message

# import forms
from forms.forms import EmailPasswordForm as epf

# Import models
from models.users import UserModel


@app.before_first_request
def create_tables():
    # db.drop_all()
    db.create_all()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about', methods=['POST','GET'])
def about():
    form = epf()
    
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)

        return redirect(url_for('about'))

    return render_template('about.html', form=form)


@app.route('/contact')
def contact():
    return render_template('contact.html')


def send_verification_email(user):
    token = user.get_verification_token()

    subject='Confirm your Email' 

    # token = ts.dumps(form.email.data, salt='email-confirm-key')

    confirm_url = url_for(
            'confirm_email',
            token=token,
            _external=True
        )

    html = render_template(
            'email/activate.html',
            confirm_url=confirm_url
        )

    msg = Message(subject, 
                    sender='noreply@demo.com', 
                    recipients=[user.email])
    msg.body = html

    mail.send(msg)

@app.route('/accounts/create', methods=['GET','POST'])
def create_account():
    form = epf()
    
    if form.validate_on_submit():
        user = UserModel(
            email = form.email.data,
            password = form.password.data
        )
        user.add_user()

        send_verification_email(user)

        # send_email(user.email, subject, html)
 
        return 'Email has been sent with instructions to verify your account'

    return render_template('/accounts/create.html', form=form)

@app.route('/confirm/<token>', methods=['POST','GET'])
def confirm_email(token):
    user = UserModel.verify_secret_token(token)
    print(user.email)
    # try:
    #     user = UserModel.verify_secret_token(token)
    #     print(user.email)
    #     # email = ts.loads(token, salt='email-confirm-key', max_age= )
    # except:
    #     return "None"
    
    UserModel.update_user(new_email=user.email, new_email_confirmed=True)
    return 'Email was successfully verified'
    
    

    