from model import Model
from game_state_manager import GameStateManager
from game_state import GameState
from player_2d import Player2D
from world_2d import World2D

class Model2D(Model):
    def __init__(self):
        super().__init__()
        self._game_state = GameStateManager(GameState.MAIN_MENU)
        self._quit = False
        self.player = Player2D()
        self._world = World2D()
        self.rectangle = [0,0]

    def update(self, user_input):
        pass

    def update_game_state(self, new_state: GameState):
        self._game_state.change_state(new_state)

    @property
    def game_state(self) -> GameState:
        return self._game_state.get_current_state()
    
    @property
    def quit(self) -> bool:
        return self._quit
    
    @quit.setter
    def quit(self, value: bool):
        self._quit = value

    