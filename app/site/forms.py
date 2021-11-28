
from flask_wtf.form import FlaskForm
from wtforms import validators
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, FileField, SubmitField
from flask_wtf.file import  FileRequired, FileAllowed


class SearchForm(FlaskForm):
    choices = [('google', 'Google'),
               ('yandex', 'Yandex'),
               ('duckduckgo', 'DuckDuckGo')]
    select = SelectField('Search:', choices=choices)
    search = StringField('')
    submit = SubmitField("Поиск")

