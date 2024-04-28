import pygame


def draw_board(screen,
               width: int,
               height: int,
               scaling_fact: float) -> None:
    """
    displays background, including board, on screen

    :param screen: Screen to display on
    :param width: Width of the window
    :param height: Height of the Window
    :param scaling_fact: Scales the entire window
    """

    screen.fill('saddlebrown')  # background colour

    for i in range(32):

        # draw light coloured squares onto screen (dark is just background)
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'beige',
                             [300 * scaling_fact - (column * 100 * scaling_fact),
                              row * 50 * scaling_fact, 50 * scaling_fact, 50 * scaling_fact])
        else:
            pygame.draw.rect(screen, 'beige',
                             [350 * scaling_fact - (column * 100 * scaling_fact),
                              row * 50 * scaling_fact, 50 * scaling_fact, 50 * scaling_fact])

        # create square borders
        for k in range(9):
            pygame.draw.line(screen, 'black', (0, 50 * k * scaling_fact),
                             (400 * scaling_fact, 50 * k * scaling_fact), 2)
            pygame.draw.line(screen, 'black', (50 * k * scaling_fact, 0),
                             (50 * k * scaling_fact, 400 * scaling_fact), 2)

    # draw golden outlines
    pygame.draw.rect(screen, 'gold',
                     [0, 400 * scaling_fact, width * scaling_fact, 50 * scaling_fact], 5)
    pygame.draw.rect(screen, 'gold',
                     [400 * scaling_fact, 0, 100 * scaling_fact, height * scaling_fact], 5)


def draw_text(screen,
              scaling_fact: float,
              turn_step: int,
              medium_font,
              big_font) -> None:
    """
    displays turn based text on board

    :param screen: Screen to display on
    :param scaling_fact: Scales the entire window
    :param turn_step: Current turn of game
    :param medium_font: Medium size text
    :param big_font: Large text
    """

    # display text (turn based)
    status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                   'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    screen.blit(big_font.render(status_text[turn_step], True, 'black'), (10 * scaling_fact, 410 * scaling_fact))
    screen.blit(medium_font.render('FORFEIT', True, 'black'), (405 * scaling_fact, 415 * scaling_fact))


def draw_pieces(all_alive: dict,
                screen,
                scaling_fact: float,
                images: dict) -> None:
    """

    :param all_alive: locations of all alive pieces
    :param screen: screen to draw on
    :param scaling_fact: Scales to screen size
    :param images: Images of all pieces

    """

    for piece in all_alive.keys():  # loop white pieces

        # handling pawn seperate because of smaller image
        if piece[1] == 'pawn':
            screen.blit(images[piece[:-1]], ((all_alive[piece][0] * 50 + 11) * scaling_fact,
                                             (all_alive[piece][1] * 50 + 15) * scaling_fact))

        # rest of the pieces
        else:
            screen.blit(images[piece[:-1]], ((all_alive[piece][0] * 50 + 5) * scaling_fact,
                                             (all_alive[piece][1] * 50 + 5) * scaling_fact))


def draw_selection(all_alive: dict,
                   screen,
                   scaling_fact: float,
                   selection: tuple) -> None:
    """
    Draws blue square around selected piece

    :param all_alive: locations of all alive pieces
    :param screen: screen to draw on
    :param scaling_fact: scaling factor for screen size
    :param selection: selected pieces

    """

    pygame.draw.rect(screen, 'blue',
                     [(all_alive[selection][0] * 50 + 1) * scaling_fact,
                      (all_alive[selection][1] * 50 + 1) * scaling_fact,
                      50 * scaling_fact, 50 * scaling_fact], 3)


def draw_captured(white_captured: list[tuple[str, str, int]],
                  black_captured: list[tuple[str, str, int]],
                  screen,
                  scaling_fact: float,
                  small_images: dict) -> None:
    """
    draws captured pieces onto screen

    :param white_captured: whites captured pieces
    :param black_captured: blacks captured pieces
    :param screen: screen to draw on
    :param scaling_fact: scales to screen size
    :param small_images: small images for each piece

    """

    for i, piece in enumerate(white_captured):
        screen.blit(small_images[piece[:-1]], (463 * scaling_fact, (10 + 25 * i) * scaling_fact))

    for i, piece in enumerate(black_captured):
        screen.blit(small_images[piece[:-1]], (410 * scaling_fact, (10 + 25 * i) * scaling_fact))


def draw_moves(legal_moves: dict,
               selection: tuple,
               screen,
               scaling_fact: float) -> None:
    """
    Draws legal moves for selected piece on screen

    :param legal_moves: list of legal moves for each piece
    :param selection: selected piece
    :param screen: screen to draw on
    :param scaling_fact: factor to scale to screen size

    """

    for move in legal_moves[selection]:
        pygame.draw.circle(screen, 'blue',
                           ((move[0] * 50 + 25) * scaling_fact,
                            (move[1] * 50 + 25) * scaling_fact), 5 * scaling_fact)


def draw_check(color: str,
               all_alive: dict,
               screen,
               scaling_fact: float) -> None:
    """
    Draws red box around king

    :param color: color of king in check during own turn
    :param all_alive: locations of all pieces
    :param screen: screen to draw on
    :param scaling_fact: scales box to size

    """

    key = (color, 'king', 0)

    pygame.draw.rect(screen, 'red', [(all_alive[key][0] * 50 + 1) * scaling_fact,
                                     (all_alive[key][1] * 50 + 1) * scaling_fact, 50 * scaling_fact,
                                     50 * scaling_fact], 5)


def draw_game_over(game_end: str,
                   font, screen,
                   scaling_fact: float) -> None:
    """
    Draws Game over text on screen

    :param game_end: In which way did the game end
    :param font: Font for text
    :param screen: screen to draw to
    :param scaling_fact: factor for scaling to size

    """

    pygame.draw.rect(screen, 'black', [100 * scaling_fact, 100 * scaling_fact, 200 * scaling_fact, 35 * scaling_fact])
    screen.blit(font.render(game_end, True, 'white'), (105 * scaling_fact, 105 * scaling_fact))
    screen.blit(font.render(f'Press SPACE to Restart!', True, 'white'), (105 * scaling_fact, 120 * scaling_fact))
