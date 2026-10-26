from flask import Blueprint, request, redirect, url_for
from database.database import Nota
from flask_login import login_required, current_user

notas = Blueprint("notas", __name__)

@notas.route("/criarnota", methods=["POST"])
@login_required
def nova_nota():
    titulo = request.form.get("notatitle")
    conteudo = request.form.get("notacontent")
    
    Nota.create(username=current_user, titulo=titulo, texto=conteudo)
    return redirect(url_for("pages.notas"))

@notas.route("/excluirnota/<int:id>")
@login_required
def deletar_nota(id):
    Nota.delete().where((Nota.id==id) & (Nota.username==current_user)).execute()
    return redirect(url_for("pages.notas"))