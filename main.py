import pygame
import sys
from settings import Settings

class Game:
    def __init__(self, window_size=(1280,720)):
        pygame.init()
        self.screen = pygame.display.set_mode(window_size)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()

            keys = pygame.key.get_pressed()





if __name__ == "__main__":
    game = Game(Settings.WINDOW_SIZE)
    game.run()