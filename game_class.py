from copy import deepcopy
from start_positions import white_normal, black_normal
from move_logic import pawn_movement, rook_movement, knight_movement, bishop_movement, king_movement, rohade_movement


class GAME:
    """

    white_pieces = {('color', 'piece', id): (alive, (x, y), Moved ), ..... }

    black_pieces = {('color', 'piece', id): (alive, (x, y), ), ..... }


    alive : boolean
    (x,y) : starting coordinates


    """

    def __init__(self,
                 white_pieces: dict[tuple[str, str, int]: list[bool, tuple[int, int]]] = white_normal,
                 black_pieces: dict[tuple[str, str, int]: list[bool, tuple[int, int]]] = black_normal):

        self.white_pieces = deepcopy(white_pieces)
        self.black_pieces = deepcopy(black_pieces)
        self.moved_pieces = {}  # When Moving a piece: self.moved_pieces.add(piece)
        self.en_passant_dict = {}
        self.promo_id = 99  # starting from high value to not interfere with normal id

    # -------------------------- Defining methods for alive and captured dictionaries
    def white_alive(self) -> dict[tuple[str, str, int]: tuple[int, int]]:

        """

        :return: {alive white piece : location, ...}

        """
        return {piece: value[1] for piece, value in self.white_pieces.items() if value[0]}

    def black_alive(self) -> dict[tuple[str, str, int]: tuple[int, int]]:
        """

        :return: {alive black piece : location, ...}

        """
        return {piece: value[1] for piece, value in self.black_pieces.items() if value[0]}

    def all_alive(self) -> dict[tuple[str, str, int]: tuple[int, int]]:
        """

        :return: {alive piece : location, ...}

        """
        return {**self.white_alive(), **self.black_alive()}

    def white_captured(self) -> list[tuple[str, str, int]]:
        """

        :return: [captured piece white, ...]

        """
        return [piece for piece, value in self.white_pieces.items() if not value[0]]

    def black_captured(self) -> list[tuple[str, str, int]]:
        """

        :return: [captured piece black, ...]

        """
        return [piece for piece, value in self.black_pieces.items() if not value[0]]

    def legal_moves(self) -> dict[tuple[str, str, int]: list[tuple[int, int]]]:
        """

        :return: {piece : [legal move, ...], ...}

        """
        legal_moves = {}

        for piece, coords in self.all_alive().items():
            move_list = []  # resetting list for each piece
            x, y = coords

            if piece[1] == 'pawn':
                move_list = pawn_movement(self, piece, x, y)

            elif piece[1] == 'rook':
                move_list = rook_movement(self, piece, x, y)

            elif piece[1] == 'knight':
                move_list = knight_movement(self, piece, x, y)

            elif piece[1] == 'bishop':
                move_list = bishop_movement(self, piece, x, y)

            elif piece[1] == 'queen':
                #  Moves like a combined bishop and rook
                list_rook = rook_movement(self, piece, x, y)
                list_bishop = bishop_movement(self, piece, x, y)
                move_list = list_rook + list_bishop

            elif piece[1] == 'king':
                king_list = king_movement(self, piece, x, y)
                rohade_list = rohade_movement(self, piece)
                move_list = king_list + rohade_list

            legal_moves[piece] = move_list

        return legal_moves

    def move(self,
             piece: tuple[str, str, int],
             target_location: tuple[int, int],
             white_locations: dict,
             black_locations: dict,
             locations: dict) \
            -> None:

        """
        Moves the selected piece to the target location, captures piece if in target location

        :param piece: piece to move
        :param target_location: location to move to
        :param white_locations: locations of white pieces
        :param black_locations: locations of black pieces
        :param locations: locations of all pieces

        """

        self.moved_pieces.add(piece)  # adds piece to moved pieces-set if not moved before

        x0, y0 = locations[piece]  # starting location
        x, y = target_location

        # Determine direction and enemies based on piece color
        is_white = piece[0] == 'white'
        direction = -1 if is_white else 1
        enemies = black_locations if is_white else white_locations

        if target_location in enemies.values():
            captured_piece = next(enemy_piece for enemy_piece, position in enemies.items()
                                  if position == target_location)
            captured = True
        elif piece[1] == 'pawn' and target_location in self.en_passant_dict.values():
            captured_piece = next(enemy_piece for enemy_piece, position in self.en_passant_dict.items()
                                  if position == target_location)
            captured = True
        else:
            captured_piece = None
            captured = False

        if (piece[1] == 'king'  # if king moves two --> Rohade
                and abs(x0 - x) == 2):

            if (x - x0) < 0:  # rohade to the left
                rook_position = (0, y)
            else:
                rook_position = (7, y)

            rook = None
            for key, value in self.all_alive().items():
                if (value == rook_position
                        and key[1] == 'rook'
                        and piece[0] == key[0]):

                    rook = key
                    break

            rook_x = x - (x - x0)/2  # rook ends up between king starting and ending position
            rook_target = (rook_x, y)

            if rook is not None:
                self.move(rook, rook_target, white_locations, black_locations, locations)

        # moving a white piece
        if is_white:
            self.white_pieces[piece][1] = target_location

            if captured:
                self.black_pieces[captured_piece][0] = False

        # moving a black piece
        else:  # piece[0] == 'black'
            self.black_pieces[piece][1] = target_location

            if captured:
                self.white_pieces[captured_piece][0] = False

        # saving double jump pawns location for en-passant
        self.en_passant_dict = {}  # resets after every move
        if piece[1] == 'pawn' and abs(y0 - y) == 2:
            self.en_passant_dict[piece] = (x0, y0 + direction)

    def promote(self,
                piece_to_promote: tuple) -> None:

        """
        Promotes pawn meant for promotion to a queen

        :param piece_to_promote: Piece meant for promotion

        """

        if piece_to_promote[0] == 'white':
            value = self.white_pieces.pop(piece_to_promote)
            self.white_pieces[('white', 'queen', self.promo_id)] = value

        else:
            value = self.black_pieces.pop(piece_to_promote)
            self.black_pieces[('black', 'queen', self.promo_id)] = value

        self.promo_id -= 1
