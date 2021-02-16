from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv
from flask_cors import CORS
import requests as r
import json
import os
import random


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
    receitas = getReceitas(str(request.args.get('i')))
    if receitas:
        return jsonify(receitas)
    else:
        return jsonify({"status":"error"})

@app.route('/receita/template/')
def receitas_template():
    receitas = getReceitas(str(request.args.get('i')))
    if receitas:
        return render_template('receitas.html',
                            receitas=receitas)
    else:
        return jsonify({"status":"error"})


@app.route('/tela-busca/')
def tela_busca():
    return render_template('tela_busca.html',nome=['gustavo','garcia','pereira'])

def getReceitas(parametro):
    url = "http://www.recipepuppy.com/api/?i={}".format(parametro)
    return json.loads(r.request('GET', url).text)['results']

#def getGifs(lista_receitas):
#    for i in range(len(lista_receitas)):
#        t = r.request('GET',"https://api.giphy.com/v1/gifs/search?api_key={}&q='{}'&limit=1&offset=0&rating=g&lang=en".format(os.getenv("GIF_API"),lista_receitas[i]['title'])).text
#    
#        for j in json.loads(t)['data']:
#            lista_receitas[i]['url-gif'] = j['images']['original']['url']
#    return lista_receitas
    

@app.route('/teste-templete/')
def teste_template():
    return render_template('conteudo.html',
                        imagem1 = "html-1.1s-47px(1).svg",
                        imagem2 = "couch-1.1s-203px.svg")

        

@app.route('/api/ppt/jogada')
def pedra_papel_tasoura():
    usuario = request.args.get('jogada_usuario')
    computador = random.choice(['pedra','papel','tesoura'])
    obj = vitoria(usuario, computador)
    return jsonify(
        obj
    )

def vitoria(usuario,computador):
    obj = {
        "usuario":"{}".format(usuario),
        "computado":"{}".format(computador),
        "vitoria":"",
        "mensagem":"",
        "img1":"",
        "img2":""
        }
    img ={
        'pedra':"https://res.cloudinary.com/dminw7meh/image/upload/v1611517829/img-jogo-site/pedra_nzefl3.svg",
        'tesoura':"https://res.cloudinary.com/dminw7meh/image/upload/v1611517830/img-jogo-site/tesoura_oulwv9.svg",
        'papel':"https://res.cloudinary.com/dminw7meh/image/upload/v1611517829/img-jogo-site/papel_rmwauk.svg",
    }
    # pe > t
    # pe < pa
    # t > pa

    #https://res.cloudinary.com/dminw7meh/image/upload/v1611517829/img-jogo-site/pedra_nzefl3.svg
    #https://res.cloudinary.com/dminw7meh/image/upload/v1611517830/img-jogo-site/tesoura_oulwv9.svg
    #https://res.cloudinary.com/dminw7meh/image/upload/v1611517829/img-jogo-site/papel_rmwauk.svg
    
    if usuario == 'pedra' and computador == 'tesoura':
        obj['vitoria'] = 'usuario'
        obj['mensagem'] = 'você venceu'
        obj['img1'] = img[usuario]
        obj['img2'] = img[computador]

    if usuario == 'tesoura' and computador == 'pedra':
        obj['vitoria'] = 'computador'
        obj['mensagem'] = 'computador venceu'
        obj['img2'] = img[computador] 
        obj['img1'] = img[usuario]

    if usuario == 'papel' and computador == 'pedra':
        obj['vitoria'] = 'usuario'
        obj['mensagem'] = 'você venceu'
        obj['img1'] = img[usuario]
        obj['img2'] = img[computador] 

    if usuario == 'pedra' and computador == 'papel':
        obj['vitoria'] = 'computador'
        obj['mensagem'] = 'computador venceu'
        obj['img2'] = img[computador] 
        obj['img1'] = img[usuario]

    if usuario == 'tesoura' and computador == 'papel':
        obj['vitoria'] = 'usuario'
        obj['mensagem'] = 'você venceu'
        obj['img1'] = img[usuario]
        obj['img2'] = img[computador] 

    if usuario == 'papel' and computador == 'tesoura':
        obj['vitoria'] = 'computador'
        obj['mensagem'] = 'computador venceu'
        obj['img2'] = img[computador] 
        obj['img1'] = img[usuario]

    if obj['vitoria']=='' and obj['mensagem'] == '':
        obj['vitoria'] = 'empate'
        obj['mensagem'] = 'deu empate'
        obj['img1'] = img[usuario]
        obj['img2'] =  img[computador] 
    
    return obj

if __name__ == '__main__':
	app.run(debug=False)