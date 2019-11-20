import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery


celery = Celery(broker='redis://localhost//')
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if not os.path.isdir('app/static/photos'):
    os.mkdir('app/static')
    os.mkdir('app/static/photos')

from app import routes, models
