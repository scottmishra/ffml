from flask import jsonify
from flask_restful import Resource

class defense(Resource):
    def get(self, name, year):
        return { 'name': name,'year': year}

class defenses(Resource):
    def get(self, year):
        return [{'year': year}]