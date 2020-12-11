from flask import Flask,jsonify
import requests as r
import json
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

import os


@app.route('/')
def hello_world():
    li = getReceitas()
    return jsonify(getGifs(li))

def getReceitas():
    url = "http://www.recipepuppy.com/api/?i=onions"
    return json.loads(r.request('GET', url).text)['results']

def getGifs(lista_receitas):
    for i in range(len(lista_receitas)):
        t = r.request('GET',"https://api.giphy.com/v1/gifs/search?api_key={}&q='{}'&limit=1&offset=0&rating=g&lang=en".format(os.getenv("GIF_API"),lista_receitas[i]['title'])).text
    
        for j in json.loads(t)['data']:
            lista_receitas[i]['url-gif'] = j['images']['480w_still']['url']
    return lista_receitas
    

if __name__ == "__main__":
    app.run(debug=True)