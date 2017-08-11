import nfldb

db = nfldb.connect()
q = nfldb.Query(db)

q.game(season_year=2017, season_type='Preseason')
for pp in q.sort('passing_yds').limit(5).as_aggregate():
    print pp.player, pp.passing_yds
