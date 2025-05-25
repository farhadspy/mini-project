##calculator

print("<<wlcome to calculator>>")
while True:
    print("pls selecte the action: ")
    result = input("(+) or (-) or (/) or (*) or (exit): ")
    if result == "exit":
        break
    x=float(input("pls enter the number: "))
    y=float(input("pls enter the number: "))
    if result == "+":
        sum = x+y
        print("result: ",sum )
    elif result == "-":
        sub = x-y
        print("result: ",sub )
    elif result == "/":
        div = x/y
        print("result: ",div )
    elif result == "*":
        mul = x*y
        print("result: ",mul )
print("tanks for use calculator.bye")
    






