class player_response(object):
    position = ""
    name = ""
    year = ""
    height = 0.0
    weight = 0.0
    yardage = {}
    touchdowns = {}

    def __init__(self, pos, name, year):
        self.position = pos
        self.name = name
        self.year = year