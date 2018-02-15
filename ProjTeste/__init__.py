from flask import Flask
from db import db

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'db':'testing', 'alias':'default'}
db.init_app(app)

import ProjTeste.views
# db.connect(teste, 'localhost:27017')