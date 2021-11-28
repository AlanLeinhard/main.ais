import subprocess

from app.models import db, User, Role, roles_users


OS = 0
SET = 0
print("Выберите тип установки:")
print("Установить БД: 1")
print("Обновить БД: 0")
input(SET)
print("Выберите вашу ОС:")
print("Windows: 1")
print("Linux: 0")
input(OS)

if SET == 1:
    if OS == 1:
        subprocess.run('set FLASK_APP=app', shell=True)
        subprocess.run('set FLASK_ENV=development', shell=True)
    else:
        subprocess.run('export FLASK_APP=app', shell=True)
        subprocess.run('export FLASK_ENV=development', shell=True)
else:

    if OS == 1:
        subprocess.run('rd -r migrations', shell=True)
        subprocess.run('set FLASK_APP=app', shell=True)
        subprocess.run('set FLASK_ENV=development', shell=True)
    else:
        subprocess.run('rm -r migrations', shell=True)
        subprocess.run('export FLASK_APP=app', shell=True)
        subprocess.run('export FLASK_ENV=development', shell=True)
subprocess.run('flask db init', shell=True)
subprocess.run('flask db migrate', shell=True)
subprocess.run('flask db upgrade', shell=True)





r = Role(name='admin', description='admin')
db.session.add(r)
db.session.commit()

r = Role(name='prepod', description='prepod')
db.session.add(r)
db.session.commit()

r = Role(name='kursant', description='kursant')
db.session.add(r)
db.session.commit()


u = User(name='admin', email='admin@admin.com', username= 'admin', password='adminadmin', active= True)
db.session.add(u)
db.session.commit()

ru = roles_users(user_id = 1, role_id = 1)
db.session.add(ru)
db.session.commit()

u = User(name='prepod', email='prepod@prepod.com', username= 'prepod', password='prepod', active= True)
db.session.add(u)
db.session.commit()

ru = roles_users(user_id = 2, role_id = 2)
db.session.add(ru)
db.session.commit()

u = User(name='kursant', email='kursant@kursant.com', username= 'kursant', password='kursant', active= True)
db.session.add(u)
db.session.commit()

ru = roles_users(user_id = 3, role_id = 3)
db.session.add(ru)
db.session.commit()
