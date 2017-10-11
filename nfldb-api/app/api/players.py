from app.helper.player_response import player_response
from flask import jsonify
from flask_restful import Resource

class players(Resource):
    def get(self, name, position, year) :
        response = player_response( position, name, year)
        return jsonify(response)