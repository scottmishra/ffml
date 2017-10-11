from flask import Flask
from flask_restful import Api

from api.players import players
from api.defenses import defenses
app = Flask(__name__)
app_api = Api(app)

app_api.add_resource(players, '/players/<string:name>/<string:position>/<string:year>')
app_api.add_resource(defenses, '/')