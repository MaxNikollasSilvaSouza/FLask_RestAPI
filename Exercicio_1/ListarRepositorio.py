import requests
import json

def requisicao_api(nome):
        resposta = requests.get(f'https://api.github.com/users/{nome}/repos')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            #caso de erro, ele retorna um status http
            return resposta.status_code

