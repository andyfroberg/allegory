class Settings:
    # Window
    WINDOW_WIDTH = 1200  # use pygame.display.Info later to get size of user's display
    WINDOW_HEIGHT = int(WINDOW_WIDTH * 0.8)
    DEFAULT_WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

    # Frames per second
    FPS = 30

    # Background colors
    BG_BLACK = (0, 0, 0)
    BG_WHITE = (255, 255, 255)
    BG_DARK_GRAY = (40, 40, 40)
    BG_DARK_BLUE_GRAY = (17, 17, 39)

    # Character movement
    PLAYER_SPEED = 5