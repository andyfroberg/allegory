import pygame
from controller.controller import Controller
from model.model_2d import Model2D
from view.view_2d import View2D
from model.game_state import GameState
from model.settings import Settings

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
        
        # Player basic movement
        direction = pygame.math.Vector2(0, 0)
        if user_input[pygame.K_w]:  # move up
            direction[1] -= Settings.PLAYER_SPEED

        if user_input[pygame.K_s]:  # move down
            direction[1] += Settings.PLAYER_SPEED

        if user_input[pygame.K_a]:  # Move left
            direction[0] -= Settings.PLAYER_SPEED

        if user_input[pygame.K_d]:  # Move right
            direction[0] += Settings.PLAYER_SPEED

        # Player jump
        if user_input[pygame.K_SPACE]:  # Jump
            pass

        self.model.player.move(direction)

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