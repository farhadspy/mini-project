# Solving a quadratic equation
import math 

def quadratic_equation(a,b,c):
    Δ = b**2 - 2*a*c

    if Δ > 0:
        x1 = (-b - math.sqrt(Δ)) / (2*a)
        x2 = (-b + math.sqrt(Δ)) / (2*a)
        print("x1: ", x1 ,"x2: " , x2)
    elif Δ == 0:
        x = -b / (2*a)
        print("x:", x)
    elif Δ < 0:
        print("no answer")
        
        
        
a = int(input("pls enter a: "))
b = int(input("pls enter b: "))
c = int(input("pls enter c: "))

quadratic_equation(a,b,c)