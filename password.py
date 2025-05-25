#password

import time
j=3
while True:
    for i in range (3):
        x=int(input("pls enter pass: "))
        if x == 1377:
            print("thats correct")
            print("welcome")
            break
        else:
            print("thats incorrect. pls try again")
            j=j-1
            print("number of try is: ",j)
    if j == 0:
        time.sleep(30)
        j=3
    else:
        break
        