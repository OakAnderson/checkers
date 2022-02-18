import pygame
from model.Board import Board
from model.Player import Player


class App:
    def __init__(self):
        self._running = True
        self._display_surf = True
        self.size = self.weight, self.height = 480, 480

        self.board = Board()
        self.white_player = Player('white')
        self.black_player = Player('black')
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self._display_surf.blit(self.board.image, (0, 0))
        self.white_player.pieces.blit(self._display_surf)
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_loop(self):
        pass

    def on_render(self):
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
