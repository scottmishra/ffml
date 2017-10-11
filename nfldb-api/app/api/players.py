from app.helper.player_response import player_response
from flask_restful import Resource

class players(Resource):
    def get(self, name, position, year):
        return {'pos':position, 'name':name,'year': year}