import os

BOARD_IMAGE_FILE = os.path.join("resources", "images", "board.svg")
BOARD_SIZE = 480
SQUARE_SIZE = (BOARD_SIZE // 8)

PIECE_IMAGE_FILE = {
    'white': os.path.join("resources", "images", "white_piece.png"),
    'black': os.path.join("resources", "images", "black_piece.png")
}
