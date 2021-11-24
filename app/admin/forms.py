from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.fields.simple import EmailField, FileField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_wtf import FlaskForm


class ServiceForm(FlaskForm):
    title = StringField('Название сервиса', [validators.Length(min=4, max=25)])
    desc = StringField('desc', [validators.Length(min=6, max=35)])
    url_serv = StringField('url_serv', [validators.Length(min=6, max=35)])
    image = FileField('image', validators=[
                      FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField("Добавить")


class NewsForm(FlaskForm):
    author_id = StringField("Заголовок новости", [
                            validators.Length(min=4, max=25)])
    title = StringField('Название сервиса', [validators.Length(min=4, max=25)])
    body = StringField('Название сервиса', [validators.Length(min=4, max=25)])
    submit = SubmitField("Добавить")


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', [
                           validators.Length(min=4, max=25)])
    password = PasswordField('Новый пароль', [
        validators.DataRequired()
    ])
    pass


class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', [
                           validators.Length(min=4, max=25)])
    email = StringField('Email-адрес', [validators.Length(min=6, max=35)])
    password = PasswordField('Новый пароль', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Пароли должны совпадать')
    ])
    confirm = PasswordField('Повторите пароль')
    pass
