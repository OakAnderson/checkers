from typing import Tuple

import pygame

from model.Board import Board
from model.Piece import Piece
from model.Constants import SQUARE_SIZE, VALID_SQUARES, BLACK


class BoardService:
    def __init__(self):
        self.piece_to_move = None
        self.last_move = BLACK
        self.down_position = None
        self.board = None

    def move_piece(self, piece: Piece, position: Tuple):
        if self.board.has_piece(position) or not self.is_valid_position(position):
            return
        
        self.board.clear_square(piece.get_position())
        self.board.set_piece_position(piece, position)
        piece.set_position(position)
    
    def normalize_position(self, position: Tuple):
        x = (position[0]//SQUARE_SIZE) * SQUARE_SIZE
        y = (position[1]//SQUARE_SIZE) * SQUARE_SIZE

        return (x, y)
    
    def is_valid_position(self, position: Tuple):
        return position in VALID_SQUARES

    def play(self, position: Tuple):
        position = self.normalize_position(position)
        if self.board.has_piece(position):
            self.piece_to_move = self.board.get_piece(position)
            return

        if self.piece_to_move is not None:
            if self.piece_to_move.color == self.last_move:
                return

            self.last_move = self.piece_to_move.color
            self.move_piece(self.piece_to_move, position)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.down_position = self.normalize_position(pygame.mouse.get_pos())
            return

        if event.type == pygame.MOUSEBUTTONUP:
            position = self.normalize_position(pygame.mouse.get_pos())
            if position != self.down_position:
                return
            
            self.play(position)
    
    def set_board(self, board: Board):
        self.board = board
