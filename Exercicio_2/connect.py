from typing_extensions import Required
from mongoengine import *
from mongoengine.connection import connect
import mongoengine
from mongoengine.document import Document

#Conexão com o banco
mongoengine.connect(host = "mongodb+srv://username:password@servername.ssha1.mongodb.net/databasename?retryWrites=true&w=majority")

#DOCUMENTO
class Colecao(Document):
    NOME = mongoengine.StringField(Required = True)
    DESCRICAO = mongoengine.StringField(Required = True)
    VALOR = mongoengine.FloatField(Required = True)
