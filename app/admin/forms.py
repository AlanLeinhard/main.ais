from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.fields.simple import EmailField, FileField, SubmitField
from flask_wtf.file import FileRequired, FileAllowed
from flask_wtf import FlaskForm
from wtforms.widgets.core import CheckboxInput


class ServiceForm(FlaskForm):
    title = StringField('Название сервиса', [validators.Length(min=4, max=25)])
    title2 = StringField('Скрытое поле', [validators.Length(min=4, max=25)])
    desc = StringField('Описание', [validators.Length(min=4)])
    url_serv = StringField('Адрес', [validators.Length(min=3)])
    image = FileField('Изображение', validators=[
                      FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField("Добавить")

class ServiceUpdForm(FlaskForm):
    title = StringField('Название')
    desc = StringField('Описание')
    url_serv = StringField('Адрес')
    image = FileField('Изображение')
    check = BooleanField("Сменить изображение")
    submit = SubmitField("Редактировать")


class ProjectForm(FlaskForm):
    title = StringField('Название проекта', [validators.Length(min=4, max=25)])
    title2 = StringField('Скрытое поле', [validators.Length(min=4, max=25)])
    desc = StringField('Описание', [validators.Length(min=4)])
    url_serv = StringField('Адрес', [validators.Length(min=3)])
    image = FileField('Изображение', validators=[
                      FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField("Добавить")


class NewsForm(FlaskForm):
    title = StringField('Новость', [validators.Length(min=4, max=25)])
    title2 = StringField('Скрытое поле', [validators.Length(min=4, max=25)])
    desc = StringField('Описание', [validators.Length(min=1)])
    body = StringField('Текст', [validators.Length(min=1)])
    image = FileField('Изображение', validators=[
                      FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField("Добавить")


class UserForm(FlaskForm):
    
    name = StringField('Новые данные ФИО', )
    username = StringField('Новое имя пользователя',)
    email = StringField('Новая электронная почта', )
    check = BooleanField("Сменить пароль")
    password = PasswordField('Новый пароль', )
    submit = SubmitField("Применить")


# class RegisterForm(FlaskForm):
#     username = StringField('Имя пользователя', [
#                            validators.Length(min=4, max=25)])
#     email = StringField('Email-адрес', [validators.Length(min=6, max=35)])
#     password = PasswordField('Новый пароль', [
#         validators.DataRequired(),
#         validators.EqualTo('confirm', message='Пароли должны совпадать')
#     ])
#     confirm = PasswordField('Повторите пароль')
#     pass
