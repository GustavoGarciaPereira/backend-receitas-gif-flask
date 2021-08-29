from flask import Flask, render_template
from dotenv import load_dotenv
from flask_cors import CORS

from jogo_p_p_t import config as config_jogo
from bioinformatica import config as config_bio
from api_feriado import config as config_feriados
from receitas import config as config_receita

load_dotenv()


def criate_app():
    app = Flask(__name__)

    CORS(app)

    config_jogo(app)
    config_bio(app)
    config_feriados(app)
    config_receita(app)

    @app.route("/")
    def home():
        nomes = ["gustavo", "garcia", "pereira"]
        titulo = "Gustavo API"
        return render_template("boas_vindas.html", nome=nomes, titulo=titulo)

    @app.route("/teste-templete/")
    def teste_template():
        return render_template(
            "conteudo.html",
            imagem1="html-1.1s-47px(1).svg",
            imagem2="couch-1.1s-203px.svg",
        )

    return app
