from abc import ABCMeta, abstractmethod
from game_state_manager import GameStateManager

class Model(metaclass=ABCMeta):
    @property
    @abstractmethod
    def game_state(self) -> GameStateManager:
        """Returns the current game state."""
        pass
    