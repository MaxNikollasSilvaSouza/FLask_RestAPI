import connect as conx

#cria a base de dados

#inserindo valores
def salvar(name, desc,valor):
    
    try:
        #SALVANDO DOCUMENTO
        variavelqq = conx.Colecao(NOME = name, DESCRICAO =desc, VALOR = valor)
        variavelqq.save()
    except Exception as e:
        print(str(e))