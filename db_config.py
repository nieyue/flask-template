# encoding:utf8
from flask_sqlalchemy import SQLAlchemy
# 数据库连接遵循这个语句
# dialect+driver://username:password@host:port/database
#此时先不传入app
db = SQLAlchemy()
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'liliu'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'myblog'

# 使用一种Python3的语法将连接数据的各种参数连接起来
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
#配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
