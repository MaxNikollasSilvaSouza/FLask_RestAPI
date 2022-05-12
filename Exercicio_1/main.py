from flask import Flask, request
from flask.scaffold import F
import ListarRepositorio as lr

app = Flask(__name__)

@app.route("/post_repositorios", methods=['POST'])
def Post_repository():
    nome = request.json
    dados_tratados =[]
    dados_misturados  = lr.requisicao_api(nome['nome'])

    dados_tratados.append(nome['nome'])
    for dado in range(len(dados_misturados)):
        dados_tratados.append(dados_misturados[dado]['name'])    
  
    return str(dados_tratados)

