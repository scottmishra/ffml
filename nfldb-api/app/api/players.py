from app.helper.player_response import player_response
from flask_restful import Resource

class player(Resource):
    def get(self, name, position, year):
        return {'pos':position, 'name':name,'year': year}

class playersByPosition(Resource):
    def get(self, position, year):
        return [{}]

class playersByYearOnly(Resource):
    def get(self, year):
        return[{'year': year}]