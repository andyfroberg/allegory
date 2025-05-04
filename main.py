import pygame
import sys
from model_2d import Model2D
from view_2d import View2D
from controller_2d import Controller2D
from game_2d import Game2D
from settings import Settings


def game_entry_point(game_type="2d"):
    if game_type == "2d":
        model = Model2D()
        view = View2D(Settings.DEFAULT_WINDOW_SIZE)
        controller = Controller2D(model, view)
        game = Game2D(model, view, controller)  # TODO: clean up - are references needed in game class?
        game.run()
    elif game_type == "3d":
        raise NotImplementedError("3D game not implemented yet.")
    else:
        raise ValueError(f"Unknown game type: {game_type}. Supported types are '2d' and '3d'.")


if __name__ == "__main__":
    game_entry_point("2d")

