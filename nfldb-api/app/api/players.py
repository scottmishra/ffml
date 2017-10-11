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
    offensive_stats = {
        'rushing': {
            'total_yds': nfldb_player.rushing_yds,
            'total_attempts': nfldb_player.rushing_att
        },
        'receiving': {
            'total_yds': nfldb_player.receiving_yds,
            'total_targets': nfldb_player.receiving_tar
        },
        'passing': {
            'total_yds': nfldb_player.passing_yds,
            'total_attempts': nfldb_player.passing_att
        },
        'return': (nfldb_player.puntret_yds + nfldb_player.kickret_yds)
    }
    scoring_stats = {
        'rushing': nfldb_player.rushing_tds,
        'receiving': nfldb_player.receiving_tds,
        'passing': nfldb_player.passing_tds,
        'return': (nfldb_player.kickret_tds + nfldb_player.puntret_tds)
    }
    profile_stats = {'name':player.full_name, 'height': player.height, 'weight': player.weight, 'years_pro': player.years_pro};

    total_stats = {
        'player': player.full_name,
        'offensive_stats': offensive_stats,
        'scoring_stats': scoring_stats,
        'profile': profile_stats
    }
    return total_stats