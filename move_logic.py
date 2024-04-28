from math import copysign


def pawn_movement(self,
                  piece: tuple[str, str, int],
                  x: int,
                  y: int) -> list[tuple[int, int]]:

    """

    :param self: Which game instance to operate on
    :param piece: Which piece to check ( Mainly important for id and color)
    :param x: x coordinate of piece
    :param y: y coordinate of piece

    :return: List of all legal moves for given piece

    """

    pawn_move_list = []  # creating list to write allowed pawn moves to

    if piece[0] == 'white':
        direction = -1  # white moves in negative direction
        enemies = self.black_alive()  # alive black pieces are whites enemy
        not_final_rank = y > 0  # defining bools for whites final ranks
        not_penultimate_rank = y > 1

    else:  # piece[0] == 'black'
        direction = 1  # black moves in positive direction
        enemies = self.white_alive()  # alive black pieces are whites enemy
        not_final_rank = y < 7  # defining bools for blacks final ranks
        not_penultimate_rank = y < 6

    # Check if pawn can capture normal or en-passant
    if (x - 1, y + direction) in enemies.values() or (x - 1, y + direction) in self.en_passant_dict.values():
        pawn_move_list.append((x - 1, y + direction))

    if (x + 1, y + direction) in enemies.values() or (x + 1, y + direction) in self.en_passant_dict.values():
        pawn_move_list.append((x + 1, y + direction))

    # Check for obstruction in front of pawn and if already on final rank
    if (x, y + direction) not in self.all_alive().values() and not_final_rank:
        pawn_move_list.append((x, y + direction))

        # Check if still allowed to move two and then check if able to
        if (piece not in self.moved_pieces and (x, y + direction * 2) not in self.all_alive().values()
                and not_penultimate_rank):
            pawn_move_list.append((x, y + direction * 2))

    return pawn_move_list  # returning list of allowed moves


def rook_movement(self,
                  piece: tuple[str, str, int],
                  x: int, y: int) -> list[tuple[int, int]]:

    """

    :param self: Which game instance to operate on
    :param piece: Which piece to check ( Mainly important for id and color)
    :param x: x coordinate of piece
    :param y: y coordinate of piece

    :return: List of all legal moves for given piece

    """

    rook_move_list = []

    if piece[0] == 'white':
        friends = self.white_alive()
        enemies = self.black_alive()

    else:  # piece[0] == 'black

        friends = self.black_alive()
        enemies = self.white_alive()

    for i in range(4):  # 4 directions (up, down, right, left)
        path_free = True
        step = 1

        if i == 0:
            dx = 0
            dy = 1
        elif i == 1:
            dx = 0
            dy = -1
        elif i == 2:
            dx = 1
            dy = 0
        else:
            dx = -1
            dy = 0

        while path_free:
            # add to valid moves in direction as long as path is free and still on board
            if ((x + (step * dx), y + (step * dy)) not in friends.values()
                    and 0 <= x + (step * dx) <= 7 and 0 <= y + (step * dy) <= 7):

                rook_move_list.append((x + (step * dx), y + (step * dy)))

                # move until on enemy piece
                if (x + (step * dx), y + (step * dy)) in enemies.values():
                    path_free = False
                step += 1

            else:
                path_free = False

    return rook_move_list


def knight_movement(self,
                    piece: tuple[str, str, int],
                    x: int,
                    y: int) -> list[tuple[int, int]]:

    """

    :param self: Which game instance to operate on
    :param piece: Which piece to check ( Mainly important for id and color)
    :param x: x coordinate of piece
    :param y: y coordinate of piece

    :return: List of all legal moves for given piece

    """

    knight_moves_list = []

    if piece[0] == 'white':
        friends_list = self.white_alive()
    else:
        friends_list = self.black_alive()
    # 2 in one direction and 1 in the perpendicular directions
    dx_dy = [(dx, dy) for dx in [-2, -1, 1, 2] for dy in [-2, -1, 1, 2] if abs(dx) != abs(dy)]

    for i in range(len(dx_dy)):
        dx, dy = dx_dy[i]
        target = (x + dx, y + dy)

        if target not in friends_list.values() and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            knight_moves_list.append(target)

    return knight_moves_list


def bishop_movement(self,
                    piece: tuple[str, str, int],
                    x: int,
                    y: int) -> list[tuple[int, int]]:

    """

    :param self: Which game instance to operate on
    :param piece: Which piece to check ( Mainly important for id and color)
    :param x: x coordinate of piece
    :param y: y coordinate of piece

    :return: List of all legal moves for given piece

    """

    bishop_move_list = []

    if piece[0] == 'white':
        friends = self.white_alive()
        enemies = self.black_alive()

    else:  # piece[0] == 'black

        friends = self.black_alive()
        enemies = self.white_alive()

    for i in range(4):  # 4 directions (up-right,up-left, down-right, down-left )
        path_free = True
        step = 1

        if i == 0:
            dx = 1
            dy = 1
        elif i == 1:
            dx = -1
            dy = 1
        elif i == 2:
            dx = 1
            dy = -1
        else:
            dx = -1
            dy = -1

        while path_free:
            # add to valid moves in direction as long as path is free and still on board
            if ((x + (step * dx), y + (step * dy)) not in friends.values()
                    and 0 <= x + (step * dx) <= 7 and 0 <= y + (step * dy) <= 7):

                bishop_move_list.append((x + (step * dx), y + (step * dy)))

                # move until on enemy piece
                if (x + (step * dx), y + (step * dy)) in enemies.values():
                    path_free = False
                step += 1

            else:
                path_free = False
    return bishop_move_list


def king_movement(self,
                  piece: tuple[str, str, int],
                  x: int,
                  y: int) -> list[tuple[int, int]]:
    """

    :param self: Which game instance to operate on
    :param piece: Which piece to check ( Mainly important for id and color)
    :param x: x coordinate of piece
    :param y: y coordinate of piece

    :return: List of all legal moves for given piece

    """

    king_moves_list = []

    if piece[0] == 'white':
        friends_list = self.white_alive()
    else:
        friends_list = self.black_alive()
    # 1 in all directions
    dx_dy = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if not (dx == 0 and dy == 0)]

    for i in range(len(dx_dy)):
        dx, dy = dx_dy[i]
        target = (x + dx, y + dy)

        if target not in friends_list.values() and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            king_moves_list.append(target)

    return king_moves_list


def rohade_movement(self,
                    king: tuple[str, str, int]) -> list[tuple[int, int]]:
    """

    :param self: Which game instance to operate on
    :param king: Which piece to check (Mainly important for id and color)

    :return: List of rohade moves for given piece

    """

    rohade_moves_list = []
    is_white = king[0] == 'white'

    king_x_position = self.all_alive()[king][0]
    king_y_position = self.all_alive()[king][1]

    if is_white:  # creating list of rooks with the same color
        rooks = list(piece for piece in self.white_alive().keys() if piece[1] == 'rook')
    else:
        rooks = list(piece for piece in self.black_alive().keys() if piece[1] == 'rook')

    for rook in rooks:
        rook_x_position = self.all_alive()[rook][0]
        rook_y_position = self.all_alive()[rook][1]

        movement_direction = int(copysign(1, rook_x_position - king_x_position))  # direction of king rohade move

        same_rank = king_y_position == rook_y_position

        path_free = True
        x_position_to_check = king_x_position
        occupied_spaces = self.all_alive().values()

        while (x_position_to_check + movement_direction) != rook_x_position and path_free:
            x_position_to_check += movement_direction  # Move the check position
            path_free = (x_position_to_check, king_y_position) not in occupied_spaces

        if (king not in self.moved_pieces  # king has not moved
                and rook not in self.moved_pieces  # rook has not moved
                and same_rank
                and path_free):

            rohade_move = (king_x_position + 2 * movement_direction, king_y_position)

            rohade_moves_list.append(rohade_move)

    return rohade_moves_list
