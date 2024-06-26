
"""
This initialy loads all packages, to check if available, with Error handling
"""
try:
    import pygame
except ModuleNotFoundError:
    print('pygame is not installed\nTry: pip install -r requirements.txt')
    exit()
except Exception as error:
    print(error)
    exit()

try:
    import copy
except ModuleNotFoundError:
    print('copy was not found')
    exit()
except Exception as error:
    print(error)
    exit()

try:
    from math import copysign
except ModuleNotFoundError:
    print('math was not found')
    exit()
except Exception as error:
    print(error)
    exit()

try:
    import os
except ModuleNotFoundError:
    print('os was not found')
    exit()
except Exception as error:
    print(error)
    exit()


"""
This checks if all Python files exist and if you have access to them.
"""
files = ['Backend.py', 'game_class.py', 'draw_functions.py', 'misc_functions.py',
         'move_logic.py', 'main_game_loop.py', 'start_positions.py']
for file in files:
    if not os.path.exists(file):
        print(f'Missing {file}')
        exit()
    elif not os.access(file, os.R_OK):
        print(f'Has no access to {file}')
        exit()
