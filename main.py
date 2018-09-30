# -*- coding: utf-8 -*-
from flask import Flask,Blueprint,request,redirect,render_template
from flask_sqlalchemy import SQLAlchemy
import db_config
from  db_config import db
from controller.UserController import userController
#创建项目对象
app = Flask(__name__)
"""
注册路由
"""
app.register_blueprint(userController,url_prefix='/user')

#bean = __import__('bean')
#session必须要设置key
app.config['SECRET_KEY']='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#环境变量，指向配置文件setting的路径
app.config.from_object(db_config)
#创建数据库对象
db.init_app(app)

@app.route('/')
def hello_world():
    if request.args.__len__()>0 and request.args['name']:
        rt=render_template('index.html',name=request.args['name'])
        return rt
    else:
        rt=render_template('index.html')
        return rt
if __name__ == '__main__':
    app.run(debug=True)