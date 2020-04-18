from flask import Flask
from flask_assets import Environment
from utils.assets import bundles
from configs.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

 
app = Flask(__name__)
assets = Environment(app)
assets.register(bundles)
app.config.from_object(Config)
mail = Mail(app)

db = SQLAlchemy(app)


from views.views import *


if __name__ == '__main__':
    app.run()