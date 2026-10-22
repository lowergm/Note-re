from flask import Flask, render_template
from database.database import db, Usuario, Nota
from routes.pages import pages
from routes.users import users
from flask_login import login_required
from extensions import lm
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")
lm.init_app(app)
lm.login_view = 'pages.login'
app.register_blueprint(pages)
app.register_blueprint(users)

@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response

@app.route("/dashboard")
def dashboard():
    usuarios = Usuario.select()
    return render_template("dashboard.html", usuarios=usuarios)

@app.route("/notas")
@login_required
def notas():
    return """
    A tela principal vem aqui
"""

if __name__ == "__main__":
    db.connect()
    db.create_tables([Usuario, Nota])
    app.run(debug=True)