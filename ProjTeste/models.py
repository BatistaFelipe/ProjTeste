from flask_mongoengine import BaseQuerySet
from mongoengine import *
from mongoengine.queryset.visitor import Q


class Fruta(Document):
	nome = StringField(required=True)
	descricao = StringField()
	preco = FloatField()