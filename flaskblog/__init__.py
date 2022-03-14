from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.config["SECRET_KEY"] = '616fbf91eac59f1026c74043044661f3'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from flaskblog import routes
# from flaskblog.models import User, Post