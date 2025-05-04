import pygame
import sys
from game import Game
from controller_2d import Controller2D
from model_2d import Model2D
from view_2d import View2D
from settings import Settings


class Game2D:
    def __init__(self, model: Model2D, view: View2D, controller: Controller2D):
        super().__init__()
        pygame.init()
        self.model = model
        self.view = view
        self.controller = controller
        self.running = None # initializing game loop sets running to True
        self.run()

    def run(self):
        self.running = True
        while self.running:
            if self.model.quit:
                pygame.quit()
                sys.exit()

            # Tell the controller to handle user input.
            self.controller.handle_user_input()

            # Get the keys the player is pressing this loop iteration.
            # user_input = self.controller.handle_user_input()
                
            # update the model based on user input from previous frame
            # self.model.update(user_input)

            # update the view based on the model
            self.view.update(self.model)

            self.view.draw()

            self.controller.clock.tick(Settings.FPS)


    def handle_user_input(self, user_input):
        pass

if __name__ == "__main__":
    pass







# # pygame setup
# pygame.init()

# screen = pygame.display.set_mode(Settings.SCREEN_DIMENSIONS)
# pygame.display.set_caption("Allegory")
# clock = pygame.time.Clock()
# running = True
# delta_time = 0

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# while running:
#     # @@ poll for events
#     # @@ pygame.QUIT event means the user clicked X to close your window
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # @@ fill the screen with a color to wipe away anything from last frame
#     screen.fill("black")

#     player_rect = pygame.Rect(player_pos, (40, 40))
#     pygame.draw.rect(screen, "green", player_rect)

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w] or keys[pygame.K_UP]:
#         player_pos.y -= 300 * delta_time
#     if keys[pygame.K_s] or keys[pygame.K_DOWN]:
#         player_pos.y += 300 * delta_time
#     if keys[pygame.K_a] or keys[pygame.K_LEFT]:
#         player_pos.x -= 300 * delta_time
#     if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
#         player_pos.x += 300 * delta_time

#     # @@ flip() the display to put your work on screen
#     pygame.display.flip()

#     # @@ limits FPS to 60
#     # @@ dt is delta time in seconds since last frame, used for framerate-
#     # @@ independent physics.
#     delta_time = clock.tick(60) / 1000

# pygame.quit()