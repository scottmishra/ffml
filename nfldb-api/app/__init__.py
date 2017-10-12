from flask import Flask
from flask_restful import Api

from api.players import *
from api.defenses import *

app = Flask(__name__)
app_api = Api(app)

app_api.add_resource(player, '/player/<string:name>/<string:year>')
app_api.add_resource(playersByPosition, '/players/<string:position>/<string:year>')
app_api.add_resource(playersByYearOnly, '/players/<string:year>')
app_api.add_resource(defense, '/defenses/<string:name>/<string:year>')
app_api.add_resource(defenses, '/defenses/<string:year>')
app_api.add_resource(playerNames, '/names/<string:position>/<string:year>')