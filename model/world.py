from abc import ABCMeta, abstractmethod

class World(metaclass=ABCMeta):
    @property
    @abstractmethod
    def world_map(self):
        pass

    @world_map.setter
    @abstractmethod
    def world_map(self, world_map):
        """
        Set the world map for the game. This should be a class that
        implements the WorldMap interface.
        """
        pass

    @abstractmethod
    def update(self):
        pass