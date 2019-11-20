import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if not os.path.isdir('./static/photos'):
    os.mkdir('static')
    os.mkdir('static/photos')

from app import routes, models
