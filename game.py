from abc import ABCMeta, abstractmethod
from model import Model
from view import View
from controller import Controller

class Game(metaclass=ABCMeta):
    @property
    @abstractmethod
    def model(self):
        """
        Implement the model for the game. This should be a class that
        implements the Model interface.
        """
        pass

    @property
    @abstractmethod
    def view(self):
        """
        Implement the view for the game. This should be a class that
        implements the View interface.
        """
        pass

    @property
    @abstractmethod
    def controller(self):
        """
        Implement the controller for the game. This should be a class that
        implements the Controller interface.
        """
        pass

    @model.setter
    @abstractmethod
    def model(self, model: Model):
        """
        Set the model for the game. This should be a class that
        implements the Model interface.
        """
        pass

    @view.setter
    @abstractmethod
    def view(self, view: View):
        """
        Set the view for the game. This should be a class that
        implements the View interface.
        """
        pass

    @controller.setter
    @abstractmethod
    def controller(self, controller: Controller):
        """
        Set the controller for the game. This should be a class that
        implements the Controller interface.
        """
        pass

    @abstractmethod
    def run(self):
        """
        Run the game loop. This should be implemented in the game class.
        """
        pass
    

 
