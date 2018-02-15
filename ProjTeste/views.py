from models import Fruta
from ProjTeste import app
from flask import render_template 

@app.route('/')
def index():
	banana = Fruta(nome='banana')
	banana.descricao = 'bananas evitam caibras'
	banana.preco = 3.50
	banana.save()

	maca = Fruta(nome='maca')
	maca.descricao = 'macas evitam caibras'
	maca.preco = 2.50
	maca.save()

	for fruta in Fruta.objects:
		print(fruta.nome)

	return render_template('index.html')
