import requests
import json
import re

from bs4 import BeautifulSoup

#url estado cidade
from flask import Blueprint, jsonify,request,render_template, abort, jsonify
from jinja2 import TemplateNotFound
import random
from collections import Counter

data_feriado = Blueprint('api_data', __name__,
                        url_prefix="/api/data_feriado")



@data_feriado.route('/')
def feriado():
    url = 'http://www.calendario.com.br/feriados-santa-maria-rs.php?ano=2021'

    #url estado
    #url = 'http://www.calendario.com.br/feriados-estado-rs.php?ano=2021'


    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    testo = soup.find_all("b")

    dic = {}
    dic2={}
    lis = []

    acha_data = re.compile(r"[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]")

    for i in range(len(testo)):
        if acha_data.match(testo[i].text.strip()):
            dic2['data'] = testo[i+0].text.strip()
            dic2['tipo'] = testo[i+1].text.strip('[]')
            dic2['descricao'] = testo[i+2].text
            dic[testo[i+0].text.strip()] = dic2
            lis.append(dic)
            dic2 = {}

    return jsonify(dic)

def config(app):
    app.register_blueprint(data_feriado)