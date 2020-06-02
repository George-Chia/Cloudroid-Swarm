from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


class Deployment(db.Model):
    __tablename__ = 'deployments'
    uid = db.Column(db.Integer, primary_key = True)
    deployment_name = db.Column(db.String(100))
    createdtime = db.Column(db.String(100))
    imagename =  db.Column(db.String(100))
    uploadname =  db.Column(db.String(100))
    username =  db.Column(db.String(100))
    firstcreatetime = db.Column(db.DateTime())
    nodeip = db.Column(db.String(20))


a = Deployment.query.all()
b = Deployment.query.filter_by(deployment_name="cloudroid").first()
c = [x.deployment_name for x in a]
print c