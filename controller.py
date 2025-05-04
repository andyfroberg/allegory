from abc import ABCMeta, abstractmethod
from model import Model
from view import View

class Controller(metaclass=ABCMeta):
    @property
    @abstractmethod
    def model(self) -> Model:
        pass

    @property
    @abstractmethod
    def view(self) -> View:
        pass

    @abstractmethod
    def handle_user_input(self):
        pass