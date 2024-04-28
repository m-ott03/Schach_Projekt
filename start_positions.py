
# Normal starting positions
white_normal = {('white', 'pawn', 0): [True, (0, 6)],
                ('white', 'pawn', 1): [True, (1, 6)],
                ('white', 'pawn', 2): [True, (2, 6)],
                ('white', 'pawn', 3): [True, (3, 6)],
                ('white', 'pawn', 4): [True, (4, 6)],
                ('white', 'pawn', 5): [True, (5, 6)],
                ('white', 'pawn', 6): [True, (6, 6)],
                ('white', 'pawn', 7): [True, (7, 6)],
                ('white', 'rook', 0): [True, (0, 7)],
                ('white', 'rook', 1): [True, (7, 7)],
                ('white', 'knight', 0): [True, (1, 7)],
                ('white', 'knight', 1): [True, (6, 7)],
                ('white', 'bishop', 0): [True, (2, 7)],
                ('white', 'bishop', 1): [True, (5, 7)],
                ('white', 'queen', 0): [True, (3, 7)],
                ('white', 'king', 0): [True, (4, 7)]
                }

black_normal = {('black', 'pawn', 0): [True, (0, 1)],
                ('black', 'pawn', 1): [True, (1, 1)],
                ('black', 'pawn', 2): [True, (2, 1)],
                ('black', 'pawn', 3): [True, (3, 1)],
                ('black', 'pawn', 4): [True, (4, 1)],
                ('black', 'pawn', 5): [True, (5, 1)],
                ('black', 'pawn', 6): [True, (6, 1)],
                ('black', 'pawn', 7): [True, (7, 1)],
                ('black', 'rook', 0): [True, (0, 0)],
                ('black', 'rook', 1): [True, (7, 0)],
                ('black', 'knight', 0): [True, (1, 0)],
                ('black', 'knight', 1): [True, (6, 0)],
                ('black', 'bishop', 0): [True, (2, 0)],
                ('black', 'bishop', 1): [True, (5, 0)],
                ('black', 'queen', 0): [True, (3, 0)],
                ('black', 'king', 0): [True, (4, 0)]
                }


# starting without a queen
white_queen_handicap = {('white', 'pawn', 0): [True, (0, 6)],
                        ('white', 'pawn', 1): [True, (1, 6)],
                        ('white', 'pawn', 2): [True, (2, 6)],
                        ('white', 'pawn', 3): [True, (3, 6)],
                        ('white', 'pawn', 4): [True, (4, 6)],
                        ('white', 'pawn', 5): [True, (5, 6)],
                        ('white', 'pawn', 6): [True, (6, 6)],
                        ('white', 'pawn', 7): [True, (7, 6)],
                        ('white', 'rook', 0): [True, (0, 7)],
                        ('white', 'rook', 1): [True, (7, 7)],
                        ('white', 'knight', 0): [True, (1, 7)],
                        ('white', 'knight', 1): [True, (6, 7)],
                        ('white', 'bishop', 0): [True, (2, 7)],
                        ('white', 'bishop', 1): [True, (5, 7)],
                        ('white', 'queen', 0): [False, (3, 7)],
                        ('white', 'king', 0): [True, (4, 7)]
                        }

black_queen_handicap = {('black', 'pawn', 0): [True, (0, 1)],
                        ('black', 'pawn', 1): [True, (1, 1)],
                        ('black', 'pawn', 2): [True, (2, 1)],
                        ('black', 'pawn', 3): [True, (3, 1)],
                        ('black', 'pawn', 4): [True, (4, 1)],
                        ('black', 'pawn', 5): [True, (5, 1)],
                        ('black', 'pawn', 6): [True, (6, 1)],
                        ('black', 'pawn', 7): [True, (7, 1)],
                        ('black', 'rook', 0): [True, (0, 0)],
                        ('black', 'rook', 1): [True, (7, 0)],
                        ('black', 'knight', 0): [True, (1, 0)],
                        ('black', 'knight', 1): [True, (6, 0)],
                        ('black', 'bishop', 0): [True, (2, 0)],
                        ('black', 'bishop', 1): [True, (5, 0)],
                        ('black', 'queen', 0): [False, (3, 0)],
                        ('black', 'king', 0): [True, (4, 0)]
                        }

#reversed ranks
white_reversed = {('white', 'pawn', 0): [True, (0, 7)],
                  ('white', 'pawn', 1): [True, (1, 7)],
                  ('white', 'pawn', 2): [True, (2, 7)],
                  ('white', 'pawn', 3): [True, (3, 7)],
                  ('white', 'pawn', 4): [True, (4, 7)],
                  ('white', 'pawn', 5): [True, (5, 7)],
                  ('white', 'pawn', 6): [True, (6, 7)],
                  ('white', 'pawn', 7): [True, (7, 7)],
                  ('white', 'rook', 0): [True, (0, 6)],
                  ('white', 'rook', 1): [True, (7, 6)],
                  ('white', 'knight', 0): [True, (1, 6)],
                  ('white', 'knight', 1): [True, (6, 6)],
                  ('white', 'bishop', 0): [True, (2, 6)],
                  ('white', 'bishop', 1): [True, (5, 6)],
                  ('white', 'queen', 0): [True, (3, 6)],
                  ('white', 'king', 0): [True, (4, 6)]
                  }

black_reversed = {('black', 'pawn', 0): [True, (0, 0)],
                ('black', 'pawn', 1): [True, (1, 0)],
                ('black', 'pawn', 2): [True, (2, 0)],
                ('black', 'pawn', 3): [True, (3, 0)],
                ('black', 'pawn', 4): [True, (4, 0)],
                ('black', 'pawn', 5): [True, (5, 0)],
                ('black', 'pawn', 6): [True, (6, 0)],
                ('black', 'pawn', 7): [True, (7, 0)],
                ('black', 'rook', 0): [True, (0, 1)],
                ('black', 'rook', 1): [True, (7, 1)],
                ('black', 'knight', 0): [True, (1, 1)],
                ('black', 'knight', 1): [True, (6, 1)],
                ('black', 'bishop', 0): [True, (2, 1)],
                ('black', 'bishop', 1): [True, (5, 1)],
                ('black', 'queen', 0): [True, (3, 1)],
                ('black', 'king', 0): [True, (4, 1)]
                }


# pawn war
white_pawn_war = {('white', 'pawn', 0): [True, (0, 6)],
                ('white', 'pawn', 1): [True, (1, 6)],
                ('white', 'pawn', 2): [True, (2, 6)],
                ('white', 'pawn', 3): [True, (3, 6)],
                ('white', 'pawn', 4): [True, (4, 6)],
                ('white', 'pawn', 5): [True, (5, 6)],
                ('white', 'pawn', 6): [True, (6, 6)],
                ('white', 'pawn', 7): [True, (7, 6)],
                ('white', 'pawn', 8): [True, (0, 7)],
                ('white', 'pawn', 9): [True, (7, 7)],
                ('white', 'pawn', 10): [True, (1, 7)],
                ('white', 'pawn', 11): [True, (6, 7)],
                ('white', 'pawn', 12): [True, (2, 7)],
                ('white', 'pawn', 13): [True, (5, 7)],
                ('white', 'pawn', 14): [True, (3, 7)],
                ('white', 'king', 0): [True, (4, 7)]
                }

black_pawn_war = {('black', 'pawn', 0): [True, (0, 1)],
                ('black', 'pawn', 1): [True, (1, 1)],
                ('black', 'pawn', 2): [True, (2, 1)],
                ('black', 'pawn', 3): [True, (3, 1)],
                ('black', 'pawn', 4): [True, (4, 1)],
                ('black', 'pawn', 5): [True, (5, 1)],
                ('black', 'pawn', 6): [True, (6, 1)],
                ('black', 'pawn', 7): [True, (7, 1)],
                ('black', 'pawn', 8): [True, (0, 0)],
                ('black', 'pawn', 9): [True, (7, 0)],
                ('black', 'pawn', 10): [True, (1, 0)],
                ('black', 'pawn', 11): [True, (6, 0)],
                ('black', 'pawn', 12): [True, (2, 0)],
                ('black', 'pawn', 13): [True, (5, 0)],
                ('black', 'pawn', 14): [True, (3, 0)],
                ('black', 'king', 0): [True, (4, 0)]
                }