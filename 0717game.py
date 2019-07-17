import turtle
scr = turtle.Screen()
Score = turtle.Turtle()
Score.hideturtle()
Barrier = turtle.Turtle()
Barrier.hideturtle()
Barrier.pensize(5)
Barrier.speed(0)
Barrier.color('red')
GJZ = turtle.Turtle()
GJZ.pensize(3)
GJZ.speed(10)

def initBarrier():
    Barrier.penup()
    Barrier.goto(-300, 300)
    Barrier.pendown()
    for i in range(4):
        Barrier.forward(600)
        Barrier.right(90)

def turnLeft():
    GJZ.left(10)

def turnRight():
    GJZ.right(10)

def inBarrier():
    if GJZ.xcor() < 300 and GJZ.xcor() > -300 and GJZ.ycor()  < 300 and GJZ.ycor() > -300:
        return True
    return False

# main starts here #
initBarrier()
scr.onkey(turnLeft, 'Left')
scr.onkey(turnRight, 'Right')
scr.listen()
step = 0
while inBarrier():
    step += 1
    Score.clear()
    Score.write('Score: ' + str(step), font = ('Arial', 15, 'normal'))
    GJZ.forward(10)
scr.exitonclick()