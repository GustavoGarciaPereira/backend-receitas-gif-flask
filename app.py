from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv
from flask_cors import CORS
import requests as r
import json
import os


load_dotenv()


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    nomes = ['gustavo','garcia','pereira']
    titulo = "Gustavo API"
    return render_template('boas_vindas.html',
                           nome=nomes,titulo=titulo)

@app.route('/receita/')
def hello_world():
    li = getReceitas(str(request.args.get('i')))
    if li:
        return jsonify(getGifs(li))
    else:
        return jsonify({"status":"error"})

@app.route('/receita/template/')
def receitas_template():
    li = getReceitas(str(request.args.get('i')))
    if li:
        return render_template('receitas.html',
                            receitas=getGifs(li))
    else:
        return jsonify({"status":"error"})


@app.route('/tela-busca/')
def tela_busca():
    return render_template('tela_busca.html',nome=['gustavo','garcia','pereira'])

def getReceitas(parametro):
    url = "http://www.recipepuppy.com/api/?i={}".format(parametro)
    return json.loads(r.request('GET', url).text)['results']

def getGifs(lista_receitas):
    for i in range(len(lista_receitas)):
        t = r.request('GET',"https://api.giphy.com/v1/gifs/search?api_key={}&q='{}'&limit=1&offset=0&rating=g&lang=en".format(os.getenv("GIF_API"),lista_receitas[i]['title'])).text
    
        for j in json.loads(t)['data']:
            lista_receitas[i]['url-gif'] = j['images']['original']['url']
    return lista_receitas
    

@app.route('/teste-templete/')
def teste_template():
    return render_template('conteudo.html',
                           imagem1 = "html-1.1s-47px(1).svg",
                           imagem2 = "couch-1.1s-203px.svg")

if __name__ == '__main__':
	app.run(debug=True)