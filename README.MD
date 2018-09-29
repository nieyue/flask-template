##pip安装virtualenv
pip install virtualenv

##第二步，创建一个独立的Python运行环境，命名为venv
virtualenv --no-site-packages venv

##新建的Python环境被放到当前目录下的venv目录。有了venv这个Python环境，可以用source进入该环境
cd venv/Scripts
activate

##web框架flask
pip install flask

##前端模板引擎jinja2
pip install jinja2

##MySQL的Python pymysql
pip install pymysql 

##MySQL的Python flask_sqlalchemy 
pip install flask-sqlalchemy 

