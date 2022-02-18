import pygame
from model.Piece import Piece
from model.Pieces import Pieces
from model.Constants import BOARD_IMAGE_FILE, VALID_SQUARES, SQUARE_SIZE


class Board:
    def __init__(self, size, white_pieces, black_pieces):
        self._image_file = BOARD_IMAGE_FILE
        self._size = size
        self.load_image()
        self._positions = {}
        self._init_positions()
        self.load_pieces(white_pieces)
        self.load_pieces(black_pieces)
    
    def load_image(self):
        self.image = pygame.image.load(self._image_file)
        self.image = pygame.transform.scale(self.image, (self._size, self._size))

    def _init_positions(self):
        for pos in VALID_SQUARES:
            self._positions[pos] = None

    def move_piece(self, piece: Piece, position):
        pos = self.normalize_position(position)
        if self.has_piece(pos) or not self.is_valid_position(pos):
            return

        self._positions[piece.get_position()] = None
        self._positions[pos] = piece
        piece.set_position(pos)

    def has_piece(self, pos):
        pos = self.normalize_position(pos)
        return pos in self._positions and self._positions[pos] is not None

    def get_piece(self, pos):
        pos = self.normalize_position(pos)
        return self._positions[pos]

    def normalize_position(self, pos):
        x = (pos[0]//SQUARE_SIZE) * SQUARE_SIZE
        y = (pos[1]//SQUARE_SIZE) * SQUARE_SIZE

        return (x, y)

    def load_pieces(self, pieces: Pieces):
        for piece in pieces.pieces:
            self._positions[piece.get_position()] = piece

    def is_valid_position(self, position):
        return position in VALID_SQUARES
