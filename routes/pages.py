from flask import Blueprint, render_template
from flask_login import login_required, current_user

pages = Blueprint("pages", __name__)

@pages.route("/")
def home():
    return render_template("index.html")

@pages.route("/login")
def login():
    return render_template("login.html")

@pages.route("/cadastrar")
def cadastrar():
    return render_template("cadastro.html")

@pages.route("/notas")
@login_required
def notas():
    return render_template("notas.html")