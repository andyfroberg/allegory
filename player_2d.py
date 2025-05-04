import pygame
from player import Player

class Player2D(Player):
    def __init__(self, 
                 initial_pos=pygame.math.Vector2(0.0, 0.0), 
                 initial_speed=0.0):
        super().__init__()
        # Initialize player attributes specific to 2D
        self._pos = initial_pos
        self._speed = initial_speed

    @property
    def pos(self) -> pygame.math.Vector2:
        """
        Implement pygame.math.Vector2 for player position in 2D space
        or pygame.math.Vector3 for player position in 3D space.
        """
        return self._pos
    
    @property
    def speed(self) -> float:
        return self._speed
    
    # @property
    # def velocity(self) -> pygame.math.Vector2:
    #     """
    #     Implement pygame.math.Vector2 for player velocity in 2D space
    #     or pygame.math.Vector3 for player velocity in 3D space.
    #     """
    #     return self._velocity

    @pos.setter
    def pos(self, *args, **kwargs):
        if args:
            if len(args) != 2:
                raise ValueError(f"Expected 2 positional arguments, got {len(args)}")
            
            if type(args[0]) is float:
                self._pos.x = args[0]
            elif type(args[0]) is int:
                self._pos.x = float(args[0])
            else:
                raise TypeError(f"Expected float or int for x, got {type(args[0])}")
            
            if type(args[1]) is float:
                self._pos.y = args[1]
            elif type(args[1]) is int:
                self._pos.y = float(args[1])
            else:
                raise TypeError(f"Expected float or int for y, got {type(args[1])}")

            return self._pos
        
        if 'x' in kwargs:
            if type(kwargs['x']) is float:
                self._pos.x = kwargs['x']
            elif type(kwargs['x']) is int:
                self._pos.x = float(kwargs['x'])
            else:
                raise TypeError(f"Expected float or int for x, got {type(kwargs['x'])}")

        if 'y' in kwargs:
            if type(kwargs['y']) is float:
                self._pos.y = kwargs['y']
            elif type(kwargs['y']) is int:
                self._pos.y = float(kwargs['y'])
            else:
                raise TypeError(f"Expected float or int for y, got {type(kwargs['y'])}")

        return self._pos
    
    @speed.setter
    def speed(self, speed: float):
        if type(speed) is float:
            self._speed = speed
        elif type(speed) is int:
            self._speed = float(speed)
        else:
            raise TypeError(f"Expected float or int for speed, got {type(speed)}")
        
        return self._speed
    
    # @velocity.setter
    # def velocity(self, *args, **kwargs):
    #     if args:
    #         if len(args) != 2:
    #             raise ValueError(f"Expected 2 positional arguments, got {len(args)}")
            
    #         if type(args[0]) is float:
    #             self._velocity.x = args[0]
    #         elif type(args[0]) is int:
    #             self._velocity.x = float(args[0])
    #         else:
    #             raise TypeError(f"Expected float or int for x, got {type(args[0])}")
            
    #         if type(args[1]) is float:
    #             self._velocity.y = args[1]
    #         elif type(args[1]) is int:
    #             self._velocity.y = float(args[1])
    #         else:
    #             raise TypeError(f"Expected float or int for y, got {type(args[1])}")

    #         return self._velocity
        
    #     if 'x' in kwargs:
    #         if type(kwargs['x']) is float:
    #             self._velocity.x = kwargs['x']
    #         elif type(kwargs['x']) is int:
    #             self._velocity.x = float(kwargs['x'])
    #         else:
    #             raise TypeError(f"Expected float or int for x, got {type(kwargs['x'])}")

    #     if 'y' in kwargs:
    #         if type(kwargs['y']) is float:
    #             self._velocity.y = kwargs['y']
    #         elif type(kwargs['y']) is int:
    #             self._velocity.y = float(kwargs['y'])
    #         else:
    #             raise TypeError(f"Expected float or int for y, got {type(kwargs['y'])}")

    #     return self._velocity
        