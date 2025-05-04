from enum import Enum

class GameState(Enum):
    GAME_PLAY = 0
    MAIN_MENU = 1
    NEW_GAME = 2
    LOAD_GAME = 3
    SAVE_GAME = 4
    LEVEL_SELECT = 5
    PAUSE_MENU = 6
    GAME_OVER = 7
    SETTINGS_MAIN = 8
    SETTINGS_CONTROLS = 9
    SETTINGS_GRAPHICS = 10
    SETTINGS_AUDIO = 11
    CREDITS = 12
    HELP = 13
    QUIT = 14
    # Add more states as needed