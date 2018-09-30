from db_config import db
"""
用户
"""
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(45),primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
#会在 SQLAlchemy 中创建一个虚拟的列，该列会与 Post.user_id (db.ForeignKey) 建立联系。这一切都交由 SQLAlchemy 自身管理
    posts = db.relationship(
        'Post',
        #用于指定表之间的双向关系，如果在一对多的关系中建立双向的关系，这样的话在对方看来这就是一个多对一的关系
        backref='users',
        #指定 SQLAlchemy 加载关联对象的方式，lazy=subquery: 会在加载 Post 对象后，将与 Post 相关联的对象全部加载
        lazy='dynamic')

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return '<Model User `{}`>'.format(self.username)

