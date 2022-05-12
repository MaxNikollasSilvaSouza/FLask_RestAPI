from flask import Flask, request
from flask.scaffold import F
import ListarRepositorio as lr
import PostProduto as P
import GetProduto as G
import DeleteProduto as D
import PutProduto as A

#ESTE CÓDIGO MAIN É RESPONSÁVEL APENAS PELAS ROTAS E DIRECIONAMENTOS!

app = Flask(__name__)

#DEFINE A ROTA E O MÉTODO

@app.route("/ex2/cadastrar", methods=['POST'])
def post_repository():
    try:
        produto = request.json
        P.salvar(produto['NOME'],produto['DESCRICAO'], produto['VALOR'])
    
        return "Produto cadastrado!"
    except:
        return 'Devido a algum problema não foi possível realizar a operação'

@app.route("/ex2/listar", methods=['GET'])
def get_repository():
    try:
        produto = request.json
        dic = G.listar(produto['NOME'])
        print(dic)

        return dic
    except:
       return 'Devido a algum problema não foi possível realizar a operação'

@app.route("/ex2/deletar", methods=['DELETE'])
def delete_repository():
    try:
        produto = request.json
        D.deletar(produto['NOME'])

        return "Produto deletado!"
    except:
       return 'Devido a algum problema não foi possível realizar a operação'

@app.route("/ex2/atualizar", methods=['PUT'])
def atualizar_repository():
    try:
        produto = request.json
        A.atualizar(produto['NOME'],produto['DESCRICAO'], produto['VALOR'])

        return "Produto atualizado!"
    except:
        return 'Devido a algum problema não foi possível realizar a operação'
