from flask import Flask
from routes.router import programming
from flask_sqlalchemy import SQLAlchemy
from config import url

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 100
app.config['SQLALCHEMY_POOL_RECYCLE'] = 280
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SQLAlchemy(app)
app.register_blueprint(programming)