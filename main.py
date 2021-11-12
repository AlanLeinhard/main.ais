from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://scott:''@localhost/flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db = SQLAlchemy(app)

class item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    inActive = db.Column(db.Boolean, default=True)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, name, inActive, tetxt):
        super().__init__()

@app.route("/")
def index():
    return render_template('index.html')

    