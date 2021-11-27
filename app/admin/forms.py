from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.fields.simple import EmailField, FileField, SubmitField
from flask_wtf.file import FileRequired, FileAllowed
from flask_wtf import FlaskForm


class ServiceForm(FlaskForm):
    title = StringField('Название сервиса', [validators.Length(min=4, max=25)])
    title2 = StringField('Скрытое поле', [validators.Length(min=4, max=25)])
    desc = StringField('Описание', [validators.Length(min=6, max=35)])
    url_serv = StringField('Адрес', [validators.Length(min=6, max=35)])
    image = FileField('Изображение', validators=[
                      FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField("Добавить")


class NewsForm(FlaskForm):
    title = StringField('Новость', [validators.Length(min=4, max=25)])
    title2 = StringField('Скрытое поле', [validators.Length(min=4, max=25)])
    desc = StringField('Описание', [validators.Length(min=6, max=35)])
    body = StringField('Текст', [validators.Length(min=4, max=25)])
    image = FileField('Изображение', validators=[
                      FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField("Добавить")


# class LoginForm(FlaskForm):
#     username = StringField('Имя пользователя', [
#                            validators.Length(min=4, max=25)])
#     password = PasswordField('Новый пароль', [
#         validators.DataRequired()
#     ])
#     pass


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
