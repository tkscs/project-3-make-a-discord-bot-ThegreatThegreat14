import random

def Bot_win():
    if not "1a" in Bot_moves and not "1b" in Bot_moves and not "1c" in Bot_moves:
        return True
    elif not "2a" in Bot_moves and not "2b" in Bot_moves and not "2c" in Bot_moves:
        return True
    elif not "3a" in Bot_moves and not "3b" in Bot_moves and not "3c" in Bot_moves:
        return True
    elif not "1a" in Bot_moves and not "2a" in Bot_moves and not "3a" in Bot_moves:
        return True
    elif not "1b" in Bot_moves and not "2b" in Bot_moves and not "3b" in Bot_moves:
        return True
    elif not "1c" in Bot_moves and not "2c" in Bot_moves and not "3c" in Bot_moves:
        return True
    elif not "1a" in Bot_moves and not "2b" in Bot_moves and not "3c" in Bot_moves:
        return True
    elif not "1c" in Bot_moves and not "2b" in Bot_moves and not "3a" in Bot_moves:
        return True
    else:
        return False
    
def Player_win():
    if not "1a" in Player_moves and not "1b" in Player_moves and not "1c" in Player_moves:
        return True
    elif not "2a" in Player_moves and not "2b" in Player_moves and not "2c" in Player_moves:
        return True
    elif not "3a" in Player_moves and not "3b" in Player_moves and not "3c" in Player_moves:
        return True
    elif not "1a" in Player_moves and not "2a" in Player_moves and not "3a" in Player_moves:
        return True
    elif not "1b" in Player_moves and not "2b" in Player_moves and not "3b" in Player_moves:
        return True
    elif not "1c" in Player_moves and not "2c" in Player_moves and not "3c" in Player_moves:
        return True
    elif not "1a" in Player_moves and not "2b" in Player_moves and not "3c" in Player_moves:
        return True
    elif not "1c" in Player_moves and not "2b" in Player_moves and not "3a" in Player_moves:
        return True
    else:
        return False
    
On_the_board = []
Player_moves = ["1a", "1b", "1c", "2a", "2b", "2c", "3a", "3b", "3c"]
Bot_moves = ["1a", "1b", "1c", "2a", "2b", "2c", "3a", "3b", "3c"]

while Bot_win == False and Player_win == False:
    if Player_moves != []:
        Bot_move = random.choice(Bot_moves)
        On_the_board = On_the_board.append(Bot_move)
        Player_moves = Player_moves - Bot_move
        Bot_moves = Bot_moves - Bot_move

        Player_move = "what the player inputted"
        On_the_board = On_the_board.append(Player_move)
        Player_moves = Player_moves - Player_move
        Bot_moves = Bot_moves - Player_move


# if player has anything in move list
## bot plays random move which gets removed from bot and player moves and added to on the board
## player enters move that gets removed from bot and player moves and added to the board

# if player or bot are missing any of the combos of three that mean a win, they win