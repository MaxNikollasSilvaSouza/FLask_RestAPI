import connect as conx
#FUNÇÃO DE ATUALIZAR VALORES
def atualizar(name, desc,valor):
    conx.Colecao.objects(NOME = name).update_one(DESCRICAO = desc)
    conx.Colecao.objects(NOME = name).update_one(VALOR = valor)
    #conx.Colecao.objects(NOME = name).update_one(NOME = name)  NÃO TEM COMO ALTERAR O NOME PQ O NOME É O IDENTIFICADOR PRINCIPAL