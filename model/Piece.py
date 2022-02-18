import pygame
import os
from model.Board import SQUARE_SIZE

PIECE_FILE = {
    'white': os.path.join("resources", "images", "white_piece.png"),
    'black': os.path.join("resources", "images", "black_piece.png")
}


class Piece:
    def __init__(self, color, x, y):
        self._image_file = PIECE_FILE[color]
        self.x, self.y = x, y
        self.load_image()
    
    def load_image(self):
        self.image = pygame.image.load(self._image_file)
        self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
    
    def blit(self, screen):
        screen.blit(self.image, (self.x, self.y))