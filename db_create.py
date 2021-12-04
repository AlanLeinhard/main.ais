import subprocess

from app.models import Post, Project, db, User, Role, roles_users, Item



# print("Установка БД: 1")
# SET=input("Обновление БД: 0")

# print("Выберите вашу ОС:")
# print("Windows: 1")
# OS=input("Linux 0:")

# if int(SET) == 0:
#     if int(OS) == 1:
#         subprocess.run('rd migrations', shell=True)
#     else:
#         subprocess.run('rm -r migrations', shell=True)
        
# if int(OS) == 1:
#     subprocess.run('set FLASK_APP=app', shell=True)
#     subprocess.run('set FLASK_ENV=development', shell=True)
# else:
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


u = User(name='admin', email='admin@admin.com',
         username='admin', password='adminadmin', active=True)
db.session.add(u)
db.session.commit()

ru = roles_users(user_id=1, role_id=1)
db.session.add(ru)
db.session.commit()

u = User(name='prepod', email='prepod@prepod.com',
         username='prepod', password='prepod', active=True)
db.session.add(u)
db.session.commit()

ru = roles_users(user_id=2, role_id=2)
db.session.add(ru)
db.session.commit()

u = User(name='kursant', email='kursant@kursant.com',
         username='kursant', password='kursant', active=True)
db.session.add(u)
db.session.commit()

ru = roles_users(user_id=3, role_id=3)
db.session.add(ru)
db.session.commit()


img = open('./start/img.png', 'rb')
image = img.read()
news = Post(author_id=1, title='Портал создан', desc='Информация',
            body="Сегодня был создан данный портал", image=image)
db.session.add(news)
db.session.commit()
print("done")


# img = open('./start/elastic.png', 'rb')
# image = img.read()
# news = Post(author_id = 1, title='Портал создан', desc='Информация', body="Сегодня был создан данный портал", image=image)
# db.session.add(news)
# db.session.commit()
# print("done")


# img = open('./start/grafana.jpg', 'rb')
# image = img.read()
# news = Post(author_id = 2, title='Портал создан', desc='Информация', body="Сегодня был создан данный портал", image=image)
# db.session.add(news)
# db.session.commit()
# print("done")


# img = open('./start/img.png', 'rb')
# image = img.read()
# news = Post(author_id = 1, title='Портал создан', desc='Информация', body="Сегодня был создан данный портал", image=image)
# db.session.add(news)
# db.session.commit()
# print("done")


# img = open('./start/runcher.jpg', 'rb')
# image = img.read()
# news = Post(author_id = 2, title='Портал создан', desc='Информация', body="Сегодня был создан данный портал", image=image)
# db.session.add(news)
# db.session.commit()
# print("done")


img = open('./start/elastic.png', 'rb')
image = img.read()
service = Item(title='Elastic', desc='DitLab кафедры АИС',
               url_serv="https://192.168.100.150:5601", image=image, active=True)
db.session.add(service)
db.session.commit()
print("done")

img = open('./start/grafana.jpg', 'rb')
image = img.read()
service = Item(title='Grafana', desc='Grafana кафедры АИС',
               url_serv="http://192.168.100.150:3005", image=image, active=True)
db.session.add(service)
db.session.commit()
print("done")

img = open('./start/postgres.jpg', 'rb')
image = img.read()
service = Item(title='Postgres', desc='Postgres кафедры АИС',
               url_serv="http://192.168.100.150:5050", image=image, active=True)
db.session.add(service)
db.session.commit()
print("done")

img = open('./start/prometheus.png', 'rb')
image = img.read()
service = Item(title='Prometheus', desc='Prometheus кафедры АИС',
               url_serv="http://192.168.100.150:9095", image=image, active=True)
db.session.add(service)
db.session.commit()
print("done")

img = open('./start/runcher.jpg', 'rb')
image = img.read()
service = Item(title='Runcher', desc='Runcher кафедры АИС',
               url_serv="https://192.168.100.150:4443", image=image, active=True)
db.session.add(service)
db.session.commit()
print("done")

img = open('./start/gitlab.jpg', 'rb')
image = img.read()
service = Item(title='GitLab', desc='GitLab кафедры АИС',
               url_serv="https://192.168.100.150:4445", image=image, active=True)
db.session.add(service)
db.session.commit()
print("done")

img = open('./start/docker.jpg', 'rb')
image = img.read()
service = Item(title='Docker', desc='Docker кафедры АИС',
               url_serv="https://192.168.100.150:8086", image=image, active=True)
db.session.add(service)
db.session.commit()
print("done")


img = open('./start/next.jpg', 'rb')
image = img.read()
service = Item(title='Nextcloud', desc='Nextcloud кафедры АИС',
               url_serv="http://192.168.100.150:8100", image=image, active=True)
db.session.add(service)
db.session.commit()
print("done")

img = open('./start/nexus.png', 'rb')
image = img.read()
service = Item(title='Nexus', desc='Nexus кафедры АИС',
               url_serv="http://192.168.100.150:8081", image=image, active=True)
db.session.add(service)
db.session.commit()
print("done")

img = open('./start/ctf.jpg', 'rb')
image = img.read()
service = Item(title='CTF', desc='CTF кафедры АИС',
               url_serv="http://192.168.100.150:8002", image=image, active=True)
db.session.add(service)
db.session.commit()
print("done")

img = open('./start/code.jpg', 'rb')
image = img.read()
service = Item(title='VS Code', desc='VS Code кафедры АИС',
               url_serv="http://192.168.100.150:8087", image=image, active=True)
db.session.add(service)
db.session.commit()
print("done")

img = open('./start/codimd.jpg', 'rb')
image = img.read()
service = Item(title='CodiMD', desc='CodiMD кафедры АИС',
               url_serv="http://192.168.100.150:3000", image=image, active=True)
db.session.add(service)
db.session.commit()
print("done")



img = open('./start/elastic.png', 'rb')
image = img.read()
project = Project(author_id="1", title='Elastic', desc='DitLab кафедры АИС',
               url_serv="https://192.168.100.150:5601", image=image, active=True)
db.session.add(project)
db.session.commit()
print("done")

img = open('./start/grafana.jpg', 'rb')
image = img.read()
project = Project(author_id="2", title='Grafana', desc='Grafana кафедры АИС',
               url_serv="http://192.168.100.150:3005", image=image, active=True)
db.session.add(project)
db.session.commit()
print("done")

img = open('./start/postgres.jpg', 'rb')
image = img.read()
project = Project(author_id="3", title='Postgres', desc='Postgres кафедры АИС',
               url_serv="http://192.168.100.150:5050", image=image, active=True)
db.session.add(project)
db.session.commit()
print("done")

img = open('./start/prometheus.png', 'rb')
image = img.read()
project = Project(author_id="1", title='Prometheus', desc='Prometheus кафедры АИС',
               url_serv="http://192.168.100.150:9095", image=image, active=True)
db.session.add(project)
db.session.commit()
print("done")

img = open('./start/runcher.jpg', 'rb')
image = img.read()
project = Project(author_id="2", title='Runcher', desc='Runcher кафедры АИС',
               url_serv="https://192.168.100.150:4443", image=image, active=True)
db.session.add(project)
db.session.commit()
print("done")

img = open('./start/gitlab.jpg', 'rb')
image = img.read()
project = Project(author_id="3", title='GitLab', desc='GitLab кафедры АИС',
               url_serv="https://192.168.100.150:4445", image=image, active=True)
db.session.add(project)
db.session.commit()
print("done")

img = open('./start/docker.jpg', 'rb')
image = img.read()
project = Project(author_id="1", title='Docker', desc='Docker кафедры АИС',
               url_serv="https://192.168.100.150:8086", image=image, active=True)
db.session.add(project)
db.session.commit()
print("done")


img = open('./start/next.jpg', 'rb')
image = img.read()
project = Project(author_id="2", title='Nextcloud', desc='Nextcloud кафедры АИС',
               url_serv="http://192.168.100.150:8100", image=image, active=True)
db.session.add(project)
db.session.commit()
print("done")

img = open('./start/nexus.png', 'rb')
image = img.read()
project = Project(author_id="3", title='Nexus', desc='Nexus кафедры АИС',
               url_serv="http://192.168.100.150:8081", image=image, active=True)
db.session.add(project)
db.session.commit()
print("done")

img = open('./start/ctf.jpg', 'rb')
image = img.read()
project = Project(author_id="1", title='CTF', desc='CTF кафедры АИС',
               url_serv="http://192.168.100.150:8002", image=image, active=True)
db.session.add(project)
db.session.commit()
print("done")

img = open('./start/code.jpg', 'rb')
image = img.read()
project = Project(author_id="2", title='VS Code', desc='VS Code кафедры АИС',
               url_serv="http://192.168.100.150:8087", image=image, active=True)
db.session.add(project)
db.session.commit()
print("done")

img = open('./start/codimd.jpg', 'rb')
image = img.read()
project = Project(author_id="3", title='CodiMD', desc='CodiMD кафедры АИС',
               url_serv="http://192.168.100.150:3000", image=image, active=True)
db.session.add(project)
db.session.commit()
print("done")
