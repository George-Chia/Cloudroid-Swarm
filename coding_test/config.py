import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'robotcloud_secret_key'

# SQLALCHEMY_DATABASE_URI = 'sqlite:///../database/robotcloud.db'
# Replace with mysql.
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'cloudroid'
PASSWORD = '1234'
HOST = '192.168.4.104'
PORT = '3306'
DATABASE = 'cloudroid'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,DATABASE)