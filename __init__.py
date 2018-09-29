# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import setting

#创建项目对象
app = Flask(__name__)

#session必须要设置key
app.config['SECRET_KEY']='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# #环境变量，指向配置文件setting的路径#创建数据库对象
app.config.from_object(setting)
db = SQLAlchemy(app)
