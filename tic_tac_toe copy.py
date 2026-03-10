import random

On_the_board = []
Player_moves = ["1a", "1b", "1c", "2a", "2b", "2c", "3a", "3b", "3c"]
Bot_moves = ["1a", "1b", "1c", "2a", "2b", "2c", "3a", "3b", "3c"]
Player_played = []
Bot_played = []

def Bot_win():
    global Bot_played
    if "1a" in Bot_played and "1b" in Bot_played and "1c" in Bot_played:
        return True
    elif "2a" in Bot_played and "2b" in Bot_played and "2c" in Bot_played:
        return True
    elif "3a" in Bot_played and "3b" in Bot_played and "3c" in Bot_played:
        return True
    elif "1a" in Bot_played and "2a" in Bot_played and "3a" in Bot_played:
        return True
    elif "1b" in Bot_played and "2b" in Bot_played and "3b" in Bot_played:
        return True
    elif "1c" in Bot_played and "2c" in Bot_played and "3c" in Bot_played:
        return True
    elif "1a" in Bot_played and "2b" in Bot_played and "3c" in Bot_played:
        return True
    elif "1c" in Bot_played and "2b" in Bot_played and "3a" in Bot_played:
        return True
    else:
        return False
    
def Player_win():
    global Player_played
    if "1a" in Player_played and "1b" in Player_played and "1c" in Player_played:
        return True
    elif "2a" in Player_played and "2b" in Player_played and "2c" in Player_played:
        return True
    elif "3a" in Player_played and "3b" in Player_played and "3c" in Player_played:
        return True
    elif "1a" in Player_played and "2a" in Player_played and "3a" in Player_played:
        return True
    elif "1b" in Player_played and "2b" in Player_played and "3b" in Player_played:
        return True
    elif "1c" in Player_played and "2c" in Player_played and "3c" in Player_played:
        return True
    elif "1a" in Player_played and "2b" in Player_played and "3c" in Player_played:
        return True
    elif "1c" in Player_played and "2b" in Player_played and "3a" in Player_played:
        return True
    else:
        return False

while True:
    if len(Player_moves) == 0:
        break
    else:
        if Player_win() == False:
            Bot_move = random.choice(Bot_moves)
            On_the_board.append(Bot_move)
            Bot_moves.remove(Bot_move)
            Player_moves.remove(Bot_move)
            Bot_played.append(Bot_move)
            print(f"bot moves {Bot_move}")
        else:
            break
        if Bot_win() == False and len(On_the_board) != 9:
            Player_move = input("play")
            On_the_board.append(Player_move)
            Player_moves.remove(Player_move)
            Bot_moves.remove(Player_move)
            Player_played.append(Player_move)
        else:
            break
if Bot_win() == True:
    print("i won")
elif Player_win() == True:
    print("you won")
else:
    print("it's a tie")


# if player has anything in move list
## bot plays random move which gets removed from bot and player moves and added to on the board
## player enters move that gets removed from bot and player moves and added to the board

# if player or bot are missing any of the combos of three that mean a win, they win