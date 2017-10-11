from app.helper.player_response import player_response
from flask_restful import Resource
from app.database.database_wrapper import Utilities

class player(Resource):
    def get(self, name, position, year):
        util = Utilities(year)
        player = util.get_player(name)[0]
        return {'name':player.player.full_name, 'height':player.player.height, 'weight':player.player.weight,
                'years_pro': player.player.years_pro}

class playersByPosition(Resource):
    def get(self, position, year):
        util = Utilities(year)
        util.print_top_receivers()
        return [{}]

class playersByYearOnly(Resource):
    def get(self, year):
        return[{'year': year}]