import pyfiglet

#pip install pyfiglet

def show():
    for row in game_bord:
        for cell in row:
            print(cell , end=" ")
        print()
        
def check():
    if game_bord[0][0] == game_bord[0][1] == game_bord[0][2] != "_":
        if Turn == 1:
            print("player 1 is winner.🎉")
            cheker = -1
            return cheker
        elif Turn == 0:
            print("player 2 is winner.🎉")
            cheker = -1
            return cheker
    elif game_bord[1][0] == game_bord[1][1] == game_bord[1][2] != "_":
        if Turn == 1:
            print("player 1 is winner.🎉")
            cheker = -1
            return cheker
        elif Turn == 0:
            print("player 2 is winner.🎉")
            cheker = -1
            return cheker
    elif game_bord[2][0] == game_bord[2][1] == game_bord[2][2] != "_":
        if Turn == 1:
            print("player 1 is winner.🎉")
            cheker = -1
            return cheker
        elif Turn == 0:
            print("player 2 is winner.🎉")
            cheker = -1
            return cheker
    elif game_bord[0][0] == game_bord[1][0] == game_bord[2][0] != "_":
        if Turn == 1:
            print("player 1 is winner.🎉")
            cheker = -1
            return cheker
        elif Turn == 0:
            print("player 2 is winner.🎉")
            cheker = -1
            return cheker
    elif game_bord[0][1] == game_bord[1][1] == game_bord[2][1] != "_":
        if Turn == 1:
            print("player 1 is winner.🎉")
            cheker = -1
            return cheker
        elif Turn == 0:
            print("player 2 is winner.🎉")
            cheker = -1
            return cheker
    elif game_bord[0][2] == game_bord[1][2] == game_bord[2][2] != "_":
        if Turn == 1:
            print("player 1 is winner.🎉")
            cheker = -1
            return cheker
        elif Turn == 0:
            print("player 2 is winner.🎉")
            cheker = -1
            return cheker
    elif game_bord[0][0] == game_bord[1][1] == game_bord[2][2] != "_":
        if Turn == 1:
            print("player 1 is winner.🎉")
            cheker = -1
            return cheker
        elif Turn == 0:
            print("player 2 is winner.🎉")
            cheker = -1
            return cheker
    elif game_bord[0][2] == game_bord[1][1] == game_bord[2][0] != "_":
        if Turn == 1:
            print("player 1 is winner.🎉")
            cheker = -1
            return cheker
        elif Turn == 0:
            print("player 2 is winner.🎉")
            cheker = -1
            return cheker
       
        
title = pyfiglet.figlet_format("TIK TOK TOE", font="slant")
print(title)

game_bord = [["_","_","_"],
             ["_","_","_"],
             ["_","_","_"]]

Turn = 1
i=0
cheker = 0
while i != 10 and cheker != -1:
    
    if i == 9 and cheker != -1:
        print("The game is tied.")
        while True:
            play_again = input("Do you want play again (yes or no): ")
            if play_again == "yes":
                Turn = 1
                i = 0
                game_bord = [["_","_","_"],
                            ["_","_","_"],
                            ["_","_","_"]]
                break
            elif play_again == "no":
                Turn = -1
                i += 1
                print("We hope you enjoyed the game.bye ")
                break
            else:
                print("pls write yes or no. ")
                
    if Turn == 1:
        print("player 1: ")   
        row = int(input("row: "))
        col = int(input("col: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_bord[row][col] == "_" :
                game_bord[row][col] = "x"
                i += 1
                show()
                cheker = check()
                Turn = 0
            else:
                print("This section is already selected.Select again: ")
        else:
            print("pls enter 0 or 1 or 2")
            
    elif Turn == 0 and cheker != -1:
        print("player 2: ")   
        row = int(input("row: "))
        col = int(input("col: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_bord[row][col] == "_" :
                game_bord[row][col] = "o"
                i += 1
                show()
                cheker = check()
                Turn = 1
            else:
                print("This section is already selected.Select again: ")
        else:
            print("pls enter 0 or 1 or 2")
            
    while cheker == -1:
        play_again = input("Do you want play again (yes or no): ")
        if play_again == "yes":
            Turn = 1
            i = 0
            cheker = 0
            game_bord = [["_","_","_"],
                        ["_","_","_"],
                        ["_","_","_"]]
            break
        elif play_again == "no":
            cheker = -1
            print("We hope you enjoyed the game.bye ")
            break
        else:
            print("pls write yes or no. ")
            