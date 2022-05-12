import connect as conx

#DELETAR DOCUMENTO
def deletar(identificacao): 
    item = conx.Colecao.objects(NOME = identificacao)
    item.delete()