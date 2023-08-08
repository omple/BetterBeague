import pygame

from systems.Visual.BoardInfo import BoardInfo
from systems.Visual.TileInfo import TileInfo


class GUI:
    running = None
    screen = None
    clock = None

    board = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True

        self.board = BoardInfo(self.screen, 0, 0)

    def killApp(self):
        pygame.quit()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.board.draw()

        pygame.display.flip()
