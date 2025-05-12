from model.game_state import GameState


class GameStateManager:
    def __init__(self, inital_state=GameState.MAIN_MENU):
        self._current_state = inital_state
        self._previous_state = None

    def get_current_state(self):
        return self._current_state

    def get_previous_state(self):
        return self._previous_state
    
    def change_state(self, new_state):
        # Shut down current state
        match self._current_state:
            case GameState.GAME_PLAY:
                pass
            case GameState.MAIN_MENU:
                pass
            case GameState.NEW_GAME:
                pass
            case GameState.LOAD_GAME:
                pass
            case GameState.SAVE_GAME:
                pass
            case GameState.LEVEL_SELECT:
                pass
            case GameState.PAUSE_MENU:
                pass
            case GameState.GAME_OVER:
                pass
            case GameState.SETTINGS_MAIN:
                pass
            case GameState.SETTINGS_CONTROLS:
                pass
            case GameState.SETTINGS_GRAPHICS:
                pass
            case GameState.SETTINGS_AUDIO:
                pass
            case GameState.CREDITS:
                pass
            case GameState.HELP:
                pass
            case GameState.QUIT:
                pass

        self._previous_state = self._current_state

        # Set up new state
        match new_state:
            case GameState.GAME_PLAY:
                pass
            case GameState.MAIN_MENU:
                pass
            case GameState.NEW_GAME:
                pass
            case GameState.LOAD_GAME:
                pass
            case GameState.SAVE_GAME:
                pass
            case GameState.LEVEL_SELECT:
                pass
            case GameState.PAUSE_MENU:
                pass
            case GameState.GAME_OVER:
                pass
            case GameState.SETTINGS_MAIN:
                pass
            case GameState.SETTINGS_CONTROLS:
                pass
            case GameState.SETTINGS_GRAPHICS:
                pass
            case GameState.SETTINGS_AUDIO:
                pass
            case GameState.CREDITS:
                pass
            case GameState.HELP:
                pass
            case GameState.QUIT:
                pass

        self._current_state = new_state
