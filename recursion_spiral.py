import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurle, lineLen):
    #if line length > 0 ,my turle walk forward
    if lineLen > 0:
        myTurle.forward(lineLen)
    #my turle turn right 90 degree
    myTurle.right(90)
    #recursion drawSpiral function
    drawSpiral(myTurle, lineLen-5)

drawSpiral(myTurtle, 100)
myWin.exitonclick()


