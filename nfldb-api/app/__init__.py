from flask import Flask
from flask_restful import Api

from api.players import players

app = Flask(__name__)
app_api = Api(app)

app_api.add_resource(players, '/player/<string:name>/<string:position>/<string:year>')