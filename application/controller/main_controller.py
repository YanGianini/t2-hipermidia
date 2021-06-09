from application.model.entity.ferramenta import Ferramenta
from application import app 
from flask import render_template, request, url_for, redirect
from application.model.dao.ferramentaDAO import FerramentaDAO

@app.route("/", methods=["GET"])
def index():
    ferramentaDAO = FerramentaDAO()
    lista_ferramentas = ferramentaDAO.lista_ferramentas()
    return render_template("index.html",lista_ferramentas=lista_ferramentas)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    ferramentaDAO = FerramentaDAO()
    lista_ferramentas = ferramentaDAO.lista_ferramentas()

    nome = request.form.get('fer_nome', None)
    link = request.form.get('fer_link', None)
    desc = request.form.get('fer_desc', None)
    tags = request.form.get('fer_tags')
    fer = Ferramenta(nome, link, desc)
    
    for i in tags:
        fer.add_tag(i)

    lista_ferramentas.append(fer)
    return redirect(url_for('index'))

@app.route("/deletar/<nome>", methods=["GET"])
def deletar(nome):
    ferramentaDAO = FerramentaDAO()
    lista_ferramentas = ferramentaDAO.lista_ferramentas()
    
    for fer in lista_ferramentas:
        if fer.get_nome() == nome:
            lista_ferramentas.remove(fer)
            return redirect(url_for('index'))

    return redirect(url_for('index')), 404    

