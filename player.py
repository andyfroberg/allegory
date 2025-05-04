from abc import ABCMeta, abstractmethod

class Player(metaclass=ABCMeta):
    @property
    @abstractmethod
    def pos(self):
        """
        Implement pygame.math.Vector2 for player position in 2D space
        or pygame.math.Vector3 for player position in 3D space.
        """
        pass

    @pos.setter
    @abstractmethod
    def pos(self, *args, **kwargs):  # TODO: do we need positional args? Maybe just use keyword args.
        pass