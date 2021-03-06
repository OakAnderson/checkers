import pygame

from model.Board import Board
from model.Player import Player
from model.Constants import BOARD_SIZE, WHITE, BLACK

from services.BoardService import BoardService


class App:
    def __init__(self):
        self.boardService = BoardService()

        self._running = True
        self._display_surf = True
        self.size = self.weight, self.height = BOARD_SIZE, BOARD_SIZE

        self.white_player = Player(WHITE)
        self.black_player = Player(BLACK)
        self.board = Board(BOARD_SIZE, self.white_player.pieces, self.black_player.pieces)
        self.boardService.set_board(self.board)

        self.positionDown = None
        self.piece_to_move = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        
        self.boardService.handle_event(event)

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.blit(self.board.image, (0, 0))
        self.white_player.pieces.blit(self._display_surf)
        self.black_player.pieces.blit(self._display_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
                self.on_loop()
                self.on_render()

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
