from flask import jsonify
from flask_restful import Resource

class defenses(Resource):
    def get(self) :
        return {'hello': 'world'}