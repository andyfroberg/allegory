import pygame
from view import View
from model_2d import Model2D
from settings import Settings

class View2D(View):
    def __init__(self, window_size=(Settings.DEFAULT_WINDOW_SIZE)):
        super().__init__()
        self._screen = pygame.display.set_mode(window_size)
        self._surface = pygame.display.get_surface()
        self._world_sprites = pygame.sprite.Group()
        self._item_sprites = pygame.sprite.Group()
        self._monster_sprites = pygame.sprite.Group()
        self._player_sprites = pygame.sprite.Group()
        self._hud_sprites = pygame.sprite.Group()
        self._ui_overlay_sprites = pygame.sprite.Group()

        self._all_sprite_groups = [self._world_sprites, 
                                  self._item_sprites, 
                                  self._monster_sprites, 
                                  self._player_sprites, 
                                  self._hud_sprites,
                                  self._ui_overlay_sprites]

    def update(self, model: Model2D):  # does this need model as an argument?
        pass
        # update world sprites

        # update item sprites

        # update monster sprites

        # update player sprites

        # update hud sprites

        # update ui overlay sprites
 

    def draw(self, model: Model2D):
        pygame.display.set_caption('Allegory') # todo: update with abstract version of displaying title (e.g., "Allegory - PAUSED")
        # https://scuba.cs.uchicago.edu/pygame/ref/sprite.html#pygame.sprite.Group
        self._screen.fill(Settings.BG_BLACK)  # todo: add contextual background colors (based on the current level or area in which the player is)
        # for sprite_group in self._all_sprite_groups:
        #     sprite_group.draw(self._screen)

        pygame.draw.rect(self._screen, (255, 0, 0), (model.rectangle[0], model.rectangle[1], 50, 50))  # Example of drawing a red rectangle

        pygame.display.flip()


    @property
    def screen(self) -> pygame.Surface:
        return self._screen

    @property
    def surface(self) -> pygame.Surface:
        return self._surface
    
    @property
    def world_sprites(self) -> pygame.sprite.Group:
        return self._world_sprites
    
    @property
    def item_sprites(self) -> pygame.sprite.Group:
        return self._item_sprites
    
    @property
    def monster_sprites(self) -> pygame.sprite.Group:
        return self._monster_sprites
    
    @property
    def player_sprites(self) -> pygame.sprite.Group:
        return self._player_sprites
    
    @property
    def hud_sprites(self) -> pygame.sprite.Group:
        return self._hud_sprites
    
    @property
    def ui_overlay_sprites(self) -> pygame.sprite.Group:
        return self._ui_overlay_sprites
    
    @property
    def all_sprite_groups(self) -> list:  # [ pygame.sprite.Group, ... ]
        return self._all_sprite_groups
    

    