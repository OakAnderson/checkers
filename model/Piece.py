import pygame
import os
from model.Constants import SQUARE_SIZE, PIECE_IMAGE_FILE


class Piece:
    def __init__(self, color, x, y):
        self._image_file = PIECE_IMAGE_FILE[color]
        self.x, self.y = x, y
        self.load_image()
    
    def load_image(self):
        self.image = pygame.image.load(self._image_file)
        self.image = pygame.transform.smoothscale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
    
    def blit(self, screen):
        screen.blit(self.image, (self.x, self.y))