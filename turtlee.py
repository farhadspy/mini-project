import turtle

turtle.bgcolor("black")
p = turtle.Pen()
colors = ["red","purple","blue","green","yellow","orange"]

i=0
while i < 360:
    for j in range(len(colors)):
        p.width(i / 100 + 1)
        p.pencolor(colors[j])
        p.forward(i)
        p.left(59)
        i += 1

turtle.done()