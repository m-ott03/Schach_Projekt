
def in_check(color: str,
             all_alive: dict,
             legal_moves: dict) -> bool:

    """
    Tests for King in check

    :param color: Which color of king to test for
    :param all_alive: locations of all alive pieces
    :param legal_moves: legal moves for all pieces

    :return: Boolean if King is in check

    """

    if color == 'white':
        king_position = all_alive[('white', 'king', 0)]
        enemy_options = [position for piece, positions in legal_moves.items()
                         if piece[0] == 'black' for position in positions]
    else:
        king_position = all_alive[('black', 'king', 0)]
        enemy_options = [position for piece, positions in legal_moves.items()
                         if piece[0] == 'white' for position in positions]

    if king_position in enemy_options:
        return True
    else:
        return False


def check_pawn_promotion(all_locations: dict) -> tuple[bool, tuple[str, str, int]]:

    """
    Checks for pawns available to promote

    :param all_locations: locations of all alive pieces

    :return: boolean(if promotion is possible), piece for which promotion is possible

    """

    for piece, location in all_locations.items():
        if piece[1] == 'pawn':
            x, y = location

            if (piece[0] == 'white' and y == 0) or (piece[0] == 'black' and y == 7):

                return True, piece

    return False, None


