import random
import os
import time

words_bank = ["book","man","freedom","sky","pc","woman","desk","table","pink","red","blue","water","blood","macbook","dog","cat","word"]
another_game = ["yes",1]

while another_game == ["yes",1]:
    good_chars =[]
    bad_chars = []
    win_user = 0
    user_mistakes = 0
    computer_choice = random.choice(words_bank)

    while user_mistakes < 6:
        win_user = 0
        os.system( 'cls' )
    
        for i in range(len(computer_choice)):
            if computer_choice[i] in good_chars:
                print(computer_choice[i],end=" ")
                win_user +=1
            else:
                print("_" , end=" ") 
                 
        if win_user != len(computer_choice):
            user_choice = input("pls guess the world: ")
            
        if len(user_choice) == 1:
            if user_choice in computer_choice:
                print("✅")
                time.sleep(1)
                good_chars.append(user_choice)
                if win_user == len(computer_choice):
                    win_user = -1
                    os.system( 'cls' )
                    break
            else:
                print("❌")
                time.sleep(1)
                user_mistakes += 1
                bad_chars.append(user_choice)
        else:
            print("pls insert one char !!")
            time.sleep(1)
            i -= 1
        
    if user_mistakes == 6:
        print("the world is: ",computer_choice)
        print("❌you are lose the game❌")
    elif win_user == -1:
        print("the world is: ",computer_choice)
        print("✅you are win the game✅")
        
    while another_game == ["yes",1]:
        another_game[0] = input("do you want to play another game (yes , no)? ")
        if another_game[0] == "yes":
            break
        elif another_game[0] == "no":
            os.system( 'cls' )
            print("tnks to play game. bye 😊")
            another_game[1] == 0
            break
        else:
            print("pls enter yes or no!!")