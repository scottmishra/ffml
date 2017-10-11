from app.helper.player_response import player_response
from flask_restful import Resource
from app.database.database_wrapper import Utilities


class player(Resource):
    def get(self, name, year):
        util = Utilities(year)
        player = util.get_player(name)[0]
        return make_player(player)


class playersByPosition(Resource):
    def get(self, position, year):
        util = Utilities(year)
        players = []
        for pp in util.get_players(position):
            player_result = make_player(pp)
            players.append(player_result)
        return players


class playersByYearOnly(Resource):
    def get(self, year):
        return[{'year': year}]



def make_player(nfldb_player):
    player = nfldb_player.player
    return {'name':player.full_name, 'height': player.height, 'weight': player.weight,
                'years_pro': player.years_pro}