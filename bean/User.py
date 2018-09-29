from __init__ import db

class User(db.Model):
    __tablename__ = 'user_tb'
    id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(10),unique=True)
    password = db.Column(db.String(16))

    def __init__(self,id,user_name,password):
        self.id = id
        self.user_name = user_name
        self.password = password
    def __repr__(self):
        return '<User %r>' % self.user_name

#db.create_all()
try:
    #增加
    # user1=User(id=4,user_name='sdf4',password='123556')
    # aa=db.session.add(user1)
    # db.session.commit()
    #查询
    users = User.query.all()
    print(users)
    #修改
    a=User.query.filter_by(user_name='sdf').update({'password':'123456'})
    db.session.commit()
    #删除
    User.query.filter_by(user_name='sdf').delete()
    db.session.commit()
except Exception:
    raise RuntimeError('第三方撒的发')
