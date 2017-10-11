import nfldb

class Utilities(object):
    'Utility class for helping de-compress the nfl game data into a easily usable python objects'

    def __init__(self, year):
        self.year = year
        # self.games = nflgame.games(self.year)
        self.db = nfldb.connect()
        self.query = nfldb.Query(self.db)

    def get_player(self, name):
        self.query.game(season_year=self.year, season_type='Regular')
        player = self.query.player(full_name=name).as_aggregate()
        return player

    def get_rushers(self):
        self.query.game(season_year=self.year, season_type='Regular')
        players = self.query.sort('rushing_yds').limit(40).as_aggregate()
        return players

    def print_top_runshers(self):
        for p in self.get_rushers():
            msg = '%s %d carries for %d yards and %d TDs'
            print msg % (p.player, p.rushing_att, p.rushing_yds, p.rushing_tds)

    def get_receivers(self):
        self.query.game(season_year=self.year, season_type='Regular')
        players = self.query.sort('receiving_yds').limit(100).as_aggregate()
        return players

    def print_top_receivers(self):
        for p in self.get_receivers():
            msg = '%s %d receptions on %d targets for %d yards and %d TDs'
            print msg % (p.player, p.receiving_rec,p.receiving_tar, p.receiving_yds, p.receiving_tds)

    def get_quarter_backs(self):
        self.query.game(season_year=self.year, season_type='Regular')
        players = self.query.sort('passing_yds').limit(40).as_aggregate()
        return players

    def print_top_quarterbacks(self):
        for p in self.get_quarter_backs():
            msg = '%s %d passes on %d attempts for %d yards and %d TDs'
            print msg % (p.player, p.passing_cmp, p.passing_att, p.passing_yds, p.passing_tds)

    def print_top_kicker(self):
        for p in self.get_kickers():
            msg = '%s %d field goals on %d attempts for %d yards'
            print msg % (p.player, p.kicking_fgm, p.kicking_fga, p.kicking_fgm_yds)


    def get_kickers(self):
        self.query.game(season_year=self.year, season_type='Regular')
        players = self.query.sort('kicking_fgm').limit(20).as_aggregate()
        return players