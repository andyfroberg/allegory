import pygame
from view.view import View
from model.model_2d import Model2D
from model.settings import Settings

from view.spritesheet import Spritesheet

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
        
        self.test_spritesheet = Spritesheet("./assets/brackeys_platformer_assets/sprites/world_tileset.png")
        self._world_floor = self.test_spritesheet.image_at((32, 32, 16, 16))

        self.player_spritesheet = Spritesheet("./assets/brackeys_platformer_assets/sprites/knight.png")
        self._p = self.player_spritesheet.image_at((9, 9, 17, 24))


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


        for i, row in enumerate(model.world.world_map):
            for j, col in enumerate(model.world.world_map[i]):
                if row[j] == 'w':
                    self._screen.blit(self._world_floor, (j*16, i*16))
                elif row[j] == ' ':
                    pygame.draw.rect(self._screen, Settings.BG_DARK_BLUE_GRAY, (j*16, i*16, 16, 16))

        # pygame.draw.circle(self._screen, (255, 0, 0), (model.player.pos[0], model.player.pos[1]), 25)  # Example of drawing a red rectangle
        self._screen.blit(self._p, (model.player.pos[0], model.player.pos[1]))

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
    

    