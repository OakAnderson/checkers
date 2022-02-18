import pygame
import os

BOARD_SIZE = 480
SQUARE_SIZE = (BOARD_SIZE // 8)


class Board:
    def __init__(self):
        self._image_file = os.path.join("resources", "images", "board.svg")
        self.load_image()
    
    def load_image(self):
        self.image = pygame.image.load(self._image_file)
