import pygame
import sys
from controller import Controller
from model_2d import Model2D
from view_2d import View2D
from game_state_manager import GameStateManager
from game_state import GameState
from settings import Settings

class Controller2D(Controller):
    def __init__(self, model: Model2D, view: View2D):
        super().__init__()
        self._model = model
        self._view = view
        self._clock = pygame.time.Clock()

    def handle_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.model.quit = True

        user_input = pygame.key.get_pressed()

        # Game state handling
        # Main menu

        # Pause menu
        if user_input[pygame.K_ESCAPE]:
                # toggle pause
                if self.model.game_state == GameState.PAUSE_MENU:
                    self.model.update_game_state(GameState.GAME_PLAY)
                else:
                    self.model.update_game_state(GameState.PAUSE_MENU)

        # Game play handling
        if user_input[pygame.K_SPACE]:  # Jump
            pass

        # -- Test movement --
        if user_input[pygame.K_w]:  # move up
            self._model.rectangle[1] -= Settings.PLAYER_SPEED

        if user_input[pygame.K_s]:  # move down
            self._model.rectangle[1] += Settings.PLAYER_SPEED

        if user_input[pygame.K_a]:  # Move left
            self._model.rectangle[0] -= Settings.PLAYER_SPEED

        if user_input[pygame.K_d]:  # Move right
            self._model.rectangle[0] += Settings.PLAYER_SPEED
        # -- End test movement --

        if user_input[pygame.K_LCTRL] and user_input[pygame.K_q]:
            self._model.quit = True  
        
        return pygame.key.get_pressed()
    
    @property
    def model(self) -> Model2D:
        return self._model
    
    @property
    def view(self) -> View2D:
        return self._view

    @property
    def clock(self) -> pygame.time.Clock:
        return self._clock