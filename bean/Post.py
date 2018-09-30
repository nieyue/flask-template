from db_config import db
"""

"""
posts_tags = db.Table('posts_tags',
        db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
        db.Column('tag_id', db.String(45), db.ForeignKey('tags.id')))


class Post(db.Model):
    """Represents Proected posts."""

    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    # Set the foreign key for Post
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))

    comments = db.relationship(
        'Comment',
        backref='posts',
        lazy='dynamic')
    # many to many: posts <==> tags
    tags = db.relationship(
        'Tag',
        #会告知 SQLAlchemy 该 many to many 的关联保存在 posts_tags 表中
        secondary=posts_tags,
        #声明表之间的关系是双向，帮助手册 help(db.backref)。
        # 需要注意的是：在 one to many 中的 backref 是一个普通的对象，
        # 而在 many to many 中的 backref 是一个 List 对象
        backref=db.backref('posts', lazy='dynamic'))
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Model Post `{}`>".format(self.title)

