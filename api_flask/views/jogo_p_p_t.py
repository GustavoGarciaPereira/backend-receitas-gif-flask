from flask import Blueprint, jsonify, request
import random

simple_simple_pagepage = Blueprint("jogo", __name__, url_prefix="/api/ppt")


@simple_simple_pagepage.route("/jogada")
def pedra_papel_tasoura():
    usuario = request.args.get("jogada_usuario")
    computador = random.choice(["pedra", "papel", "tesoura"])
    obj = vitoria(usuario, computador)
    return jsonify(obj)


def vitoria(usuario, computador):

    obj = {
        "usuario": "{}".format(usuario),
        "computado": "{}".format(computador),
        "vitoria": "",
        "mensagem": "",
        "img1": "",
        "img2": "",
    }
    img = {
        "pedra": "https://res.cloudinary.com/dminw7meh/image\
/upload/v1611517829/img-jogo-site/pedra_nzefl3.svg",
        "tesoura": "https://res.cloudinary.com/dminw7meh/image\
/upload/v1611517830/img-jogo-site/tesoura_oulwv9.svg",
        "papel": "https://res.cloudinary.com/dminw7meh/image\
/upload/v1611517829/img-jogo-site/papel_rmwauk.svg",
    }
    # pe > t
    # pe < pa
    # t > pa

    # https://res.cloudinary.com/dminw7meh/image/upload/v1611517829/img-jogo-site/pedra_nzefl3.svg
    # https://res.cloudinary.com/dminw7meh/image/upload/v1611517830/img-jogo-site/tesoura_oulwv9.svg
    # https://res.cloudinary.com/dminw7meh/image/upload/v1611517829/img-jogo-site/papel_rmwauk.svg

    if usuario == "pedra" and computador == "tesoura":
        obj["vitoria"] = "usuario"
        obj["mensagem"] = "você venceu"
        obj["img1"] = img[usuario]
        obj["img2"] = img[computador]

    if usuario == "tesoura" and computador == "pedra":
        obj["vitoria"] = "computador"
        obj["mensagem"] = "computador venceu"
        obj["img2"] = img[computador]
        obj["img1"] = img[usuario]

    if usuario == "papel" and computador == "pedra":
        obj["vitoria"] = "usuario"
        obj["mensagem"] = "você venceu"
        obj["img1"] = img[usuario]
        obj["img2"] = img[computador]

    if usuario == "pedra" and computador == "papel":
        obj["vitoria"] = "computador"
        obj["mensagem"] = "computador venceu"
        obj["img2"] = img[computador]
        obj["img1"] = img[usuario]

    if usuario == "tesoura" and computador == "papel":
        obj["vitoria"] = "usuario"
        obj["mensagem"] = "você venceu"
        obj["img1"] = img[usuario]
        obj["img2"] = img[computador]

    if usuario == "papel" and computador == "tesoura":
        obj["vitoria"] = "computador"
        obj["mensagem"] = "computador venceu"
        obj["img2"] = img[computador]
        obj["img1"] = img[usuario]

    if obj["vitoria"] == "" and obj["mensagem"] == "":
        obj["vitoria"] = "empate"
        obj["mensagem"] = "deu empate"
        obj["img1"] = img[usuario]
        obj["img2"] = img[computador]

    return obj


def config(app):
    app.register_blueprint(simple_simple_pagepage)
