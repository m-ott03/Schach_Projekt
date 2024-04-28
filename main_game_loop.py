# Scale Entire Window to size
scaling_fact = 1.8  # optimized for 1.8

# choosing  frame rate
fps = 60

try:
    from Backend import *
except ModuleNotFoundError:
    print(f'Missing Files')
    exit()
except Exception as error:
    print(error)

"""
choose your starting position. lowerst uncommented one for each colour gets choosen.
Defaults to normal position if all are commented
"""
# -------- Queen handicap
# from start_positions import white_queen_handicap as white_start_position  # white
# from start_positions import black_queen_handicap as black_start_position  # black

# -------- reversed ranks
# from start_positions import white_reversed as white_start_position  # white
# from start_positions import black_reversed as black_start_position  # black

# -------- pawn war
# from start_positions import white_pawn_war as white_start_position  # white
# from start_positions import black_pawn_war as black_start_position  # black


# Initialise GAME instance
Game = GAME(white_start_position, black_start_position)

# creating fixed list, (mainly for drawing)
# updated when needed, removes need to rerun GAME.methods every screen update
active_legal_moves = Game.legal_moves()
active_all_alive = Game.all_alive()
active_white_alive = Game.white_alive()
active_black_alive = Game.black_alive()
active_white_captured = Game.white_captured()
active_black_captured = Game.black_captured()

# main game loop
run = True
frame_count = 0
while run:
    timer.tick(fps)  # caps loop to run at frame rate

    # --------------------------------------------------- Drawing screen

    draw_board(screen, WIDTH, HEIGHT, scaling_fact)  # Draws board
    draw_text(screen, scaling_fact, turn_step, medium_font, big_font)  # Draws turn based text
    draw_pieces(active_all_alive, screen, scaling_fact, images)  # Draws pieces and selection

    if selection is not None:
        draw_selection(active_all_alive, screen, scaling_fact, selection)  # Draws red square around selected piece

    draw_captured(active_white_captured, active_black_captured,
                  screen, scaling_fact, small_images)  # Draws captured pieces

    if turn_step == 1 or turn_step == 3:  # draws available moves for selected piece
        draw_moves(active_legal_moves, selection, screen, scaling_fact)

    # Draw check box for currently playing color
    if turn_step < 2:
        color = 'white'
    else:
        color = 'black'
    if not game_over and in_check(color, active_all_alive, active_legal_moves):
        draw_check(color, active_all_alive, screen, scaling_fact)

    # Draw Game over screen
    if game_over:
        draw_game_over(game_end, font, screen, scaling_fact)

    #  ------------------------------------------------------------------------ Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:  # Handle clicks on screen
            x_coord = event.pos[0] // (50 * scaling_fact)
            y_coord = event.pos[1] // (50 * scaling_fact)
            click_coords = (x_coord, y_coord)

            # --------------------------------------  white's turns

            if turn_step == 0 or turn_step == 1:

                if click_coords == (8, 8) or click_coords == (9, 8):  # forfeit white
                    game_end = 'black won'

                # ------------- white's piece selection
                if turn_step == 0:
                    for key, coords in active_white_alive.items():

                        if click_coords == coords:
                            selection = key
                            break  # Exit loop once a match is found
                        else:
                            selection = None

                    if selection is not None:
                        turn_step += 1

                # ------------- white's move selection
                elif turn_step == 1:
                    if click_coords in active_legal_moves[selection]:
                        # move piece
                        Game.move(selection, click_coords, active_white_alive, active_black_alive, active_all_alive)

                        active_all_alive = Game.all_alive()

                        # Handle promotion
                        promotion, promo_piece = check_pawn_promotion(active_all_alive)
                        if promotion:
                            Game.promote(promo_piece)

                        selection = None
                        turn_step += 1

                        # update lists now that something might have changed
                        active_legal_moves = Game.legal_moves()
                        active_all_alive = Game.all_alive()
                        active_white_alive = Game.white_alive()
                        active_black_alive = Game.black_alive()
                        active_white_captured = Game.white_captured()
                        active_black_captured = Game.black_captured()

                    else:  # switching piece selection

                        for key, coords in active_white_alive.items():
                            if click_coords == coords:
                                selection = key

            # --------------------------------------  black's turns
            else:  # turn_step == 2 or turn_step == 3:

                if click_coords == (8, 8) or click_coords == (9, 8):  # forfeit white
                    game_end = 'white won'

                # ------------black's piece selection
                if turn_step == 2:
                    for key, coords in active_black_alive.items():

                        if click_coords == coords:
                            selection = key
                            break  # Exit loop once a match is found
                        else:
                            selection = None

                    if selection is not None:
                        turn_step += 1

                # ------------- black's move selection
                elif turn_step == 3:
                    if click_coords in active_legal_moves[selection]:
                        # move piece
                        Game.move(selection, click_coords, active_white_alive, active_black_alive, active_all_alive)

                        active_all_alive = Game.all_alive()

                        # Handle promotion
                        promotion, promo_piece = check_pawn_promotion(active_all_alive)
                        if promotion:
                            Game.promote(promo_piece)

                        selection = None
                        turn_step = 0

                        # update lists now that something might have changed
                        active_white_alive = Game.white_alive()
                        active_black_alive = Game.black_alive()
                        active_all_alive = Game.all_alive()

                        active_white_captured = Game.white_captured()
                        active_black_captured = Game.black_captured()

                        active_legal_moves = Game.legal_moves()

                    else:  # switching piece selection

                        for key, coords in active_black_alive.items():
                            if click_coords == coords:
                                selection = key

        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # Reset after Game over
            # Reset running variables
            game_end = ''
            game_over = False
            turn_step = 0

            # setup new game instance
            Game = GAME(white_start_position, black_start_position)
            active_legal_moves = Game.legal_moves()
            active_all_alive = Game.all_alive()
            active_white_alive = Game.white_alive()
            active_black_alive = Game.black_alive()
            active_white_captured = Game.white_captured()
            active_black_captured = Game.black_captured()

    # Handle Game Over
    if not ('white', 'king', 0) in active_all_alive.keys():
        game_end = 'black won'
        game_over = True
    elif not ('black', 'king', 0) in active_all_alive.keys():
        game_end = 'white won'
        game_over = True

    pygame.display.flip()  # flip to display
