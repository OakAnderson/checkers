import pygame
from model.Constants import BOARD_IMAGE_FILE


class Board:
    def __init__(self):
        self._image_file = BOARD_IMAGE_FILE
        self.load_image()
    
    def load_image(self):
        self.image = pygame.image.load(self._image_file)
