import requests
# alexa
from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, "/ludopedia")

myToken = ""

def getLudoData(myToken,apiURI):
    apiURL = "https://www.ludopedia.com.br/api/v1"
    #myToken = "xxx"

    head = {'Authorization': 'token {}'.format(myToken)}
    response = requests.get(apiURL+apiURI, headers=head)
    return response




@app.route('/')
def homepage():
    return "site ok!"


@ask.launch 
def start_skill():
    msg = "Bem vindo ao Ludopedia! O que deseja?"
    return question(msg)

@ask.intent("NewsIntent")
def getnews():
    msg = getLudoNews()
    head_msg = "As noticias sao: {}".format(msg)
    return statement(head_msg)

@ask.intent("ColecaoIntent")
def getLudoColecao():
    lista = []
    #colecao, lista_desejos, favoritos,jogados, nota, comentados
    #/colecao?lista=lista_desejos
    response = getLudoData(myToken,apiURI)
    return response

@ask.intent("ColecaoFavIntent")
def getLudoColecaoFav():
    lista = []
    #colecao, lista_desejos, favoritos,jogados, nota, comentados
    apiURI = "/colecao?lista=favoritos" 
    response = getLudoData(myToken,apiURI)
    return response

@ask.intent("JogoIntent")
def getLudoJogo():
    lista = []
    return response


@ask.intent("JogatinaIntent")
def getLudoJogatina():
    lista = []
    return response



if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)

