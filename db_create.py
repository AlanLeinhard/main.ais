from os import name
import subprocess
from flask.helpers import url_for

from flask_sqlalchemy import model
from itsdangerous import url_safe
from app.models import Post, db, User, Role, roles_users, Item


# subprocess.run('rm -r migrations', shell=True)
# subprocess.run('set FLASK_APP=app', shell=True)
# subprocess.run('set FLASK_ENV=development', shell=True)
# subprocess.run('flask db init', shell=True)
# subprocess.run('flask db migrate', shell=True)
# subprocess.run('flask db upgrade', shell=True)





# r = Role(name='admin', description='admin')
# db.session.add(r)
# db.session.commit()

# r = Role(name='prepod', description='prepod')
# db.session.add(r)
# db.session.commit()

# r = Role(name='kursant', description='kursant')
# db.session.add(r)
# db.session.commit()


# u = User(name='admin', email='admin@admin.com', username= 'admin', password='adminadmin', active= True)
# db.session.add(u)
# db.session.commit()

# ru = roles_users(user_id = 1, role_id = 1)
# db.session.add(ru)
# db.session.commit()

# u = User(name='prepod', email='prepod@prepod.com', username= 'prepod', password='prepod', active= True)
# db.session.add(u)
# db.session.commit()

# ru = roles_users(user_id = 2, role_id = 2)
# db.session.add(ru)
# db.session.commit()

# u = User(name='kursant', email='kursant@kursant.com', username= 'kursant', password='kursant', active= True)
# db.session.add(u)
# db.session.commit()

# ru = roles_users(user_id = 3, role_id = 3)
# db.session.add(ru)
# db.session.commit()



# img = open('img.png', 'rb')
# image = img.read()
# service = Item(title='qwertyuio', desc='admqwertyuioin', url_serv="qwertyuioiuytrertyuioiuytre", image=image)
# db.session.add(service)
# db.session.commit()
# print("done")

img = open('img.png', 'rb')
image = img.read()
news = Post(author_id = 3, title='qwertyucxhgio', desc='admqxcgnwertyuioin', body="qwertyuioiuytrertyuioxcfbiuytre", image=image)
db.session.add(news)
db.session.commit()
print("done")