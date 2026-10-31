from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

pages = Blueprint("pages", __name__)

@pages.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("pages.notas"))
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