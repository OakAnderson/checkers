import pygame

from typing import Tuple

from model.Piece import Piece
from model.Pieces import Pieces
from model.Constants import BOARD_IMAGE_FILE, VALID_SQUARES, SQUARE_SIZE


class Board:
    def __init__(self, size, white_pieces, black_pieces):
        self._image_file = BOARD_IMAGE_FILE
        self._size = size
        self._positions = {}

        self.load_image()
        self._init_positions()

        self.load_pieces(white_pieces)
        self.load_pieces(black_pieces)
    
    def load_image(self):
        self.image = pygame.image.load(self._image_file)
        self.image = pygame.transform.scale(self.image, (self._size, self._size))

    def _init_positions(self):
        for pos in VALID_SQUARES:
            self._positions[pos] = None

    def has_piece(self, position: Tuple):
        return position in self._positions and self._positions[position] is not None

    def get_piece(self, position: Tuple):
        return self._positions[position]

    def load_pieces(self, pieces: Pieces):
        for piece in pieces.pieces:
            self._positions[piece.get_position()] = piece
    
    def clear_square(self, position: Tuple):
        self._positions[position] = None

    def set_piece_position(self, piece: Piece, position: Tuple):
        self._positions[position] = piece
