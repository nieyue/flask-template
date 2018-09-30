# import Flask Script object
from flask_script.__init__ import Manager, Server
from flask_migrate.__init__ import Migrate, MigrateCommand
import main
from bean import User
from bean import Post
from bean import Comment
from bean import Tag

"""
通过 manager.py 来执行命令行是十分有必要的，
因为一些 Flask 的扩展只有在 Flask app object 被创建之后才会被初始化，
所以非常依赖于应用上下文的环境，在没有 Flask app object 时，
直接运行默认的 Python CLI 会导致这些 Flask 扩展返回错误。
"""
# Init manager object via app object

manager = Manager(main.app)
migrate = Migrate(main.app,main.db)
# Create a new commands: server
# This command will be run the Flask development_env server
manager.add_command("server", Server())

manager.add_command("db", MigrateCommand)

@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    # 确保有导入 Flask app object，否则启动的 CLI 上下文中仍然没有 app 对象
    return dict(app=main.app,
                db=main.db,
                User=User,
                Post=Post,
                Comment=Comment,
                Tag=Tag
                )

if __name__ == '__main__':
    manager.run()

