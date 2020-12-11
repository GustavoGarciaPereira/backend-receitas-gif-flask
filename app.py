from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_cors import CORS
import requests as r
import json
import os

load_dotenv()
app = Flask(__name__)
CORS(app)

@app.route('/')
def gustavo():
    return """
        <img src='https://lh3.googleusercontent.com/proxy/3qbOZoq2VIx_L9pOUfsBmV1qg-ER-sXemoELZXFPuddVgLcKA3GY72PLbuPH69jF6jDnIohuQKqgK_9CViP6XwMMg-W9zV2plb1XWTRv9wAYqa2BpRrllwcXTN2lcxdW9PpXG7Ip7B3lLOpvl5OU7tM63foMqK0zICRBRY4'>
        <p>Para usar a API</p>
        <p>Tem que acessar o link</p>
        <p>Passando os ingredientes como mostrado no exemplo abaixo.</p>
        <a target="_blank" href="https://deploy-flask-1.herokuapp.com/receita/?i=onion,tomato">
            https://deploy-flask-1.herokuapp.com/receita/?i=onion,tomato
        </a>
        """

@app.route('/receita/')
def hello_world():
    li = getReceitas(str(request.args.get('i')))
    if li:
        return jsonify(getGifs(li))
    else:
        return jsonify({"status":"error"})


def getReceitas(parametro):
    url = "http://www.recipepuppy.com/api/?i={}".format(parametro)
    return json.loads(r.request('GET', url).text)['results']

def getGifs(lista_receitas):
    for i in range(len(lista_receitas)):
        t = r.request('GET',"https://api.giphy.com/v1/gifs/search?api_key={}&q='{}'&limit=1&offset=0&rating=g&lang=en".format(os.getenv("GIF_API"),lista_receitas[i]['title'])).text
    
        for j in json.loads(t)['data']:
            lista_receitas[i]['url-gif'] = j['images']['480w_still']['url']
    return lista_receitas
    

if __name__ == '__main__':
	app.run(debug=True)