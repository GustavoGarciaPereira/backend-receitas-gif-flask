import json
import requests as r

from flask import Blueprint, jsonify, request, render_template


receitas = Blueprint("receita", __name__, url_prefix="/api")


@receitas.route("/receita/")
def hello_world():
    receitas = getReceitas(str(request.args.get("i")))
    if receitas:
        return jsonify(receitas)
    else:
        return jsonify({"status": "error"})


@receitas.route("/receita/template/")
def receitas_template():
    receitas = getReceitas(str(request.args.get("i")))
    if receitas:
        return render_template("receitas.html", receitas=receitas)
    else:
        return jsonify({"status": "error"})


@receitas.route("/tela-busca/")
def tela_busca():
    return render_template(
        "tela_busca.html",
        nome=["gustavo", "garcia", "pereira"])


def getReceitas(parametro):

    url = "http://www.recipepuppy.com/api/?i={}".format(parametro)
    try:
        return json.loads(r.request("GET", url).text)["results"]
    except Exception:
        return {"error": 400}


def config(app):
    app.register_blueprint(receitas)
