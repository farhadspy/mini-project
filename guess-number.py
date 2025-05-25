#guess-number

import random

computer_number = random.randint(20,500)
for i in range(100):
    user_number = int(input("pls guess: "))
    if computer_number == user_number:
        print("congratulations your win")
        print("🎉")
        break
    elif computer_number > user_number:
        print("go up and try again")
        print("⬆️")
    elif computer_number < user_number:
        print("go down and try again")
        print("⬇️")
    elif i==100:
        print("game over")
        print("you are lose")


