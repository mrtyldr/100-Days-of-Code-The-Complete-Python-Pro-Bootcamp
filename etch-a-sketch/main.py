from turtle import Turtle, Screen

muratcan = Turtle()
screen = Screen()


def move_forward():
    muratcan.forward(10)


def turn_left():
    muratcan.left(10.0)


def turn_right():
    muratcan.right(10.0)


def move_backward():
    muratcan.backward(10)


def clear_screen():
    screen.clearscreen()
    muratcan.home()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(move_backward, "s")
screen.onkey(clear_screen, "c")

screen.exitonclick()