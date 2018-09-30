#-*- coding: utf-8 -*-
from main import Blueprint, request
from bean.User import User
from db_config import db
from util.Result import Result
import json
userController=Blueprint("userController",__name__)
@userController.route('/test/<int:id>/<string:name>',methods=['GET','POST'])
def test(id,name):
    print(request.full_path)
    print(request.path)
    print(request.args['232'])
    print(request.values)
    print(request.view_args)
    print(request.form)
    return 'dfs'

"""
用户增加
"""
@userController.route('/add',methods=['GET','POST'])
def add():
    try:
        id=request.args.get('id')
        username=request.args.get('username')
        password=request.args.get('password')
        #增加
        user=User(id=id,username=username,password=password)
        db.session.add(user)
        db.session.commit()
        #return Result.getJson(user)
        return Result.getResult(200,'成功',[{'id':id,'username':username,'password':password}])
    except Exception:
        db.session.rollback()
        return Result.getResult(40000,'增加失败')
"""
用户修改
"""
@userController.route('/update',methods=['GET','POST'])
def update():
    try:
        #增加
        # user1=User(id=4,username='sdf4',password='123556')
        # aa=db.session.add(user1)
        # db.session.commit()
        #查询
        users = User.query.all()
        print(users)
        #修改
        a=User.query.filter_by(username='sdf').update({'password':'123456'})
        db.session.commit()
        #删除
        User.query.filter_by(username='sdf').delete()
        db.session.commit()
        return 'sdf'
    except Exception:
        raise RuntimeError('第三方撒的发')
