#pip安装virtualenv
pip install virtualenv

#第二步，创建一个独立的Python运行环境，命名为venv
virtualenv --no-site-packages venv

#新建的Python环境被放到当前目录下的venv目录。有了venv这个Python环境，可以用source进入该环境
cd venv/Scripts
activate

#web框架flask
pip install flask

#flask-script 是 Flask 的一个扩展，它能够创建指令，并且让这些指令在 Flask 的应用上下文中执行，可以达到修改 Flask 对象的目的
pip install flask-script

#保证原有数据完整性的情况下更新的数据库结构或将数据库回滚到之前的某一个时刻以便复现环境
pip install flask-migrate

#MySQL的Python pymysql
pip install pymysql 

#MySQL的Python flask_sqlalchemy 
pip install flask-sqlalchemy 

