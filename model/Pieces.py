from model.Piece import Piece
from model.Constants import VALID_SQUARES, WHITE, BLACK


class Pieces:
    def __init__(self, color):
        self._color = color
        self.pieces = []
        self._init_pieces()

    def _init_pieces(self):
        if self._color == WHITE:
            self._init_white_pieces()
        elif self._color == BLACK:
            self._init_black_pieces()

    def _init_white_pieces(self):
        for i in range(12):
            x, y = VALID_SQUARES[i]

            new = Piece(self._color, x, y)
            self.pieces.append(new)
    
    def _init_black_pieces(self):
        for i in range(31, 19, -1):
            x, y = VALID_SQUARES[i]

            new = Piece(self._color, x, y)
            self.pieces.append(new)
    
    def blit(self, screen):
        for piece in self.pieces:
            piece.blit(screen)
