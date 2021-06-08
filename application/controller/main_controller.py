from application import app 
from flask import render_template, request, url_for
from application.model.dao.ferramentaDAO import FerramentaDAO

@app.route("/")
def index():
    ferramentaDAO = FerramentaDAO()
    lista_ferramentas = ferramentaDAO.lista_ferramentas()
    return render_template("index.html",lista_ferramentas=lista_ferramentas)
