from flask import Flask
from database.database import db, Usuario, Nota
from routes.pages import pages
from routes.users import users
from routes.notas import notas
import flask_login
from extensions import lm
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder="templates/static")

app.secret_key = os.getenv("SECRET_KEY")
lm.init_app(app)
lm.login_view = 'pages.login'
app.register_blueprint(pages)
app.register_blueprint(users)
app.register_blueprint(notas)

@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response

if __name__ == "__main__":
    db.connect()
    db.create_tables([Usuario, Nota])
    app.run(debug=True)