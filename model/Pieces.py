from model.Piece import Piece
from model.Board import BOARD_SIZE, SQUARE_SIZE


class Pieces:
    def __init__(self, color):
        self._color = color
        self.pieces = []
        self._init_pieces()

    def _init_pieces(self):
        for i in range(12):
            x = i%4
            y = i//4

            X_pos = (x * SQUARE_SIZE)
            X_pos = X_pos + SQUARE_SIZE*x if i % 2 != 0 else X_pos
            Y_pos = (y * SQUARE_SIZE)

            if (y) % 2 == 0:
                x += SQUARE_SIZE

            print(x, y)
            new = Piece(self._color, X_pos, Y_pos)
            self.pieces.append(new)
    
    def blit(self, screen):
        for piece in self.pieces:
            piece.blit(screen)
