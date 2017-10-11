import os
from app.helper.player_response import player_response
from flask import jsonify

class players(object):
    def get(self, name, position, year) :
        response = player_response( position, name, year)
        return jsonify(response)