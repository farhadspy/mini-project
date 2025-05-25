#rock_paper_scissors

import random

score_user = 0
score_computer = 0

while 1 == 1:
    x = random.randint(1,3)
    user_choice = input("pls chose the rock_paper_scissors or exit: ")
    if x == 1:
        computer_choice = "rock"
    elif x == 2:
        computer_choice = "paper"
    elif x == 3:
        computer_choice = "scissors"
    
    if user_choice == "exit":
        print("score of user:",score_user)
        print("score of computer:",score_computer)
        if score_user == score_computer:
            print("The game is tied and there is no winner.")
        if score_user > score_computer:
            print("The winner is: user with ",score_user,"points")
        if score_user > score_computer:
            print("The winner is: computer with ",score_computer,"points")
        print("tnks and bye")
        break
    elif computer_choice == "rock" and user_choice == "paper":
        print("The user scored 👦")
        score_user = score_user + 1
    elif computer_choice == "rock" and user_choice == "scissors":
        print("The computer scored 💻")
        score_computer = score_computer + 1
    elif computer_choice == "paper" and user_choice == "rock":
        print("The computer scored 💻")
        score_computer = score_computer + 1
    elif computer_choice == "scissors" and user_choice == "rock":
        print("The user scored 👦")
        score_user = score_user + 1
    elif computer_choice == "paper" and user_choice == "scissors":
        print("The user scored 👦")
        score_user = score_user + 1
    elif computer_choice == "scissors" and user_choice == "paper":
        print("The computer scored 💻")
        score_computer = score_computer + 1
    else:
        print("equaled 🟰")
        print("try again")
    