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
    tags = request.form.get('fer_tags', None).split(", ")

    fer = Ferramenta(nome, link, desc)
       
    for tag in tags:
        fer.add_tag(tag)   
    
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


@app.route("/filtrar")
def filtrar():
    ferramentaDAO = FerramentaDAO()
    lista_ferramentas = ferramentaDAO.lista_ferramentas()
    lista_filtrada = []
    param = request.args.get("parametro_busca")
    checked = request.args.get("only_tag")

    for ferramenta in lista_ferramentas:
        if checked != "only_tag":
            if param in ferramenta.get_nome() or param in ferramenta.get_descricoes() or param in ferramenta.get_tags():
                lista_filtrada.append(ferramenta)
        else:
            if param in ferramenta.get_tags():
                lista_filtrada.append(ferramenta)

    return render_template("index.html", lista_ferramentas=lista_filtrada)





