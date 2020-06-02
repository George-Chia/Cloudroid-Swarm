from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db, models
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
a = models.Deployment.query.all()
b = models.Deployment.query.filter_by(deployment_name="cloudroid").first()
print a[0].deployment_name