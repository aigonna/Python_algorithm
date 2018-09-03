import turtle

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen) # turtle walk forward branch length
        t.right(20) #turn right 20 degree
        tree(branchLen - 15, t) #branch length minus 15, update as step 1
        t.left(40) #turn left 40 degree(two times of 20 degree)
        tree(branchLen - 15, t)
        t.right(20)
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("red")
    tree(75, t)
    myWin.exitonclick()


if __name__ == "__main__":
    main()
