# ----------Importing modules and packages
# checking if everything is available
try:
    from Package_and_file_check import *
except ModuleNotFoundError:
    print(f'Missing Package_and_file_check.py')
    exit()
except Exception as error:
    print(error)

from draw_functions import (draw_board, draw_text, draw_pieces, draw_captured, draw_selection, draw_moves,
                            draw_check, draw_game_over)
from game_class import GAME
from misc_functions import in_check, check_pawn_promotion

from start_positions import white_normal as white_start_position
from start_positions import black_normal as black_start_position

# ---------------------- initialising variables
turn_step = 0
"""
    This variable stores the current game state:

      - 0: White piece selection phase
      - 1: White piece movement phase
      - 2: Black piece selection phase
      - 3: Black piece movement phase

    **Design Choice:**

    Separating turn phases might introduce some redundancy in the code. However,
    this approach prioritizes readability and maintainability.
"""

game_end = ''
selection = None
game_over = False


# ----------------- setting up pygame window

pygame.init()

# Window size
scaling_fact = 1.8  # optimized for 1.8
WIDTH = 500 * scaling_fact
HEIGHT = 450 * scaling_fact
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# timer for frame-rate
timer = pygame.time.Clock()

# window name
pygame.display.set_caption('Two-Player Pygame Chess!')

# fonts
font = pygame.font.Font('freesansbold.ttf', int(10 * scaling_fact))
medium_font = pygame.font.Font('freesansbold.ttf', int(20 * scaling_fact))
big_font = pygame.font.Font('freesansbold.ttf', int(25 * scaling_fact))


# --------------------- loading chess pieces

# load in game piece images (queen, king, rook, bishop, knight, pawn) black and white
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (40 * scaling_fact, 40 * scaling_fact))
black_queen_small = pygame.transform.scale(black_queen, (23 * scaling_fact, 23 * scaling_fact))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (40 * scaling_fact, 40 * scaling_fact))
black_king_small = pygame.transform.scale(black_king, (23 * scaling_fact, 23 * scaling_fact))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (40 * scaling_fact, 40 * scaling_fact))
black_rook_small = pygame.transform.scale(black_rook, (23 * scaling_fact, 23 * scaling_fact))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (40 * scaling_fact, 40 * scaling_fact))
black_bishop_small = pygame.transform.scale(black_bishop, (23 * scaling_fact, 23 * scaling_fact))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (40 * scaling_fact, 40 * scaling_fact))
black_knight_small = pygame.transform.scale(black_knight, (23 * scaling_fact, 23 * scaling_fact))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (33 * scaling_fact, 33 * scaling_fact))
black_pawn_small = pygame.transform.scale(black_pawn, (23 * scaling_fact, 23 * scaling_fact))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (40 * scaling_fact, 40 * scaling_fact))
white_queen_small = pygame.transform.scale(white_queen, (23 * scaling_fact, 23 * scaling_fact))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (40 * scaling_fact, 40 * scaling_fact))
white_king_small = pygame.transform.scale(white_king, (23 * scaling_fact, 23 * scaling_fact))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (40 * scaling_fact, 40 * scaling_fact))
white_rook_small = pygame.transform.scale(white_rook, (23 * scaling_fact, 23 * scaling_fact))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (40 * scaling_fact, 40 * scaling_fact))
white_bishop_small = pygame.transform.scale(white_bishop, (23 * scaling_fact, 23 * scaling_fact))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (40 * scaling_fact, 40 * scaling_fact))
white_knight_small = pygame.transform.scale(white_knight, (23 * scaling_fact, 23 * scaling_fact))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (33 * scaling_fact, 33 * scaling_fact))
white_pawn_small = pygame.transform.scale(white_pawn, (23 * scaling_fact, 23 * scaling_fact))

images = {('white', 'pawn'): white_pawn, ('white', 'queen'): white_queen,
          ('white', 'king'): white_king, ('white', 'knight'): white_knight,
          ('white', 'rook'): white_rook, ('white', 'bishop'): white_bishop,
          ('black', 'pawn'): black_pawn, ('black', 'queen'): black_queen,
          ('black', 'king'): black_king, ('black', 'knight'): black_knight,
          ('black', 'rook'): black_rook, ('black', 'bishop'): black_bishop}

small_images = {('white', 'pawn'): white_pawn_small, ('white', 'queen'): white_queen_small,
                ('white', 'king'): white_king_small, ('white', 'knight'): white_knight_small,
                ('white', 'rook'): white_rook_small, ('white', 'bishop'): white_bishop_small,
                ('black', 'pawn'): black_pawn_small, ('black', 'queen'): black_queen_small,
                ('black', 'king'): black_king_small, ('black', 'knight'): black_knight_small,
                ('black', 'rook'): black_rook_small, ('black', 'bishop'): black_bishop_small}
