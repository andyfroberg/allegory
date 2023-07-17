from settings import Settings
from map import Map


class Player:
    def __init__(self, name="Player1"):
        self.name = name
        self.x = Settings.PLAYER_START_X
        self.y = Settings.PLAYER_START_Y

    
    def move(self, map, dx, dy):
