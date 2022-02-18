from model.Pieces import Pieces

class Player:
    def __init__(self, color):
        self._color = color
        self.pieces = Pieces(color)
    
    def blit_pieces(self, screen):
        self.pieces.blit(screen)
