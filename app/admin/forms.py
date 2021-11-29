from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.fields.simple import EmailField, FileField, SubmitField
from flask_wtf.file import FileRequired, FileAllowed
from flask_wtf import FlaskForm


class ServiceForm(FlaskForm):
    title = StringField('Название сервиса', [validators.Length(min=4, max=25)])
    title2 = StringField('Скрытое поле', [validators.Length(min=4, max=25)])
    desc = StringField('Описание')
    url_serv = StringField('Адрес')
    image = FileField('Изображение', validators=[
                      FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField("Добавить")


class NewsForm(FlaskForm):
    title = StringField('Новость', [validators.Length(min=4, max=25)])
    title2 = StringField('Скрытое поле', [validators.Length(min=4, max=25)])
    desc = StringField('Описание')
    body = StringField('Текст')
    image = FileField('Изображение', validators=[
                      FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField("Добавить")


class UserForm(FlaskForm):
    name = StringField('Новые данные ФИО', [
        validators.Length(min=4, max=25)])
    username = StringField('Новое имя пользователя', [
        validators.Length(min=4, max=25)])
    email = StringField('Новая электронная почта', [
        validators.Length(min=4, max=25)])
    password = PasswordField('Новый пароль', [
        validators.Length(min=4, max=25)])
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
