from flask import Blueprint, jsonify,request,render_template, abort
from jinja2 import TemplateNotFound
import random
from collections import Counter

bioinformatica = Blueprint('contagem', __name__,
                        url_prefix="/api/bio")


@bioinformatica.route('/contagem')
def contagem_bases():
    mapa_contagem = Counter(request.args.get('base'))

    return jsonify(
        [
            {'status':'ok'},
            {'contagem':mapa_contagem}
        ]
    )



@bioinformatica.route('/rna')
def rna_bases():
    base_dna = request.args.get('base')
    base_dna = base_dna.upper()
    mapa_contagem = {
        "A":"A",
        "C":"C",
        "T":"U",
        "G":"G"
    }
    
    saida = ""
    for letra in base_dna:
        saida += mapa_contagem[letra]
    
    return jsonify(
        [
            {'status':'ok'},
            {'base_rna':saida}
        ]
    )

@bioinformatica.route('/base_inversa')
def bases_inversa():
    base_dna = str(request.args.get('base'))

    base_dna = base_dna.upper()[::-1]
    mapa_contagem = {
        "A":"T",
        "C":"G",
        "T":"A",
        "G":"C"
    }

    saida = ""
    for letra in base_dna:
        saida += mapa_contagem[letra]


    
    return jsonify(
        [
            {'status':'ok'},
            {'base_inversa':saida}
        ]
    )


def config(app):
    app.register_blueprint(bioinformatica)
