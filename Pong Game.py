# Python code for Pong Game using Turtle module
import turtle
import winsound

# Creating a window for the game
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  # Turtle is class name and turtle is the module we imported
paddle_a.speed(0)  # this is the speed of animation for turtle module, it sets the speed to maximum possible speed
# and it's not the speed of the  paddle
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # penup moves without drawing lines
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # ball moves up by 0.2 pixels, d means change or delta
ball.dy = 0.2  # ball moves down by 0.2 pixels, d means change delta

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()  # penup because we don't want to draw a line when the pen moves
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))


# function for moving paddle 'a' upwards
def paddle_a_up():
    y = paddle_a.ycor()  # ycor returns y co-ordinate from turtle module
    y += 20  # it will add 20 pixels to the y co-ordinate
    paddle_a.sety(y)  # set the y of the paddle to the new y co-ordinate


# function for moving paddle 'a' downwards
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# function for moving paddle 'b' upwards
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


# function for moving paddle 'b' downwards
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
win.listen()                            # this line listens to the keyboard's input
win.onkeypress(paddle_a_up, "w")        # when user presses 'w' call the function paddle_a_up
win.onkeypress(paddle_a_down, "s")      # when user presses 's' call the function paddle_a_down
win.onkeypress(paddle_b_up, "Up")       # when user presses 'up' arrow call the function paddle_b_up
win.onkeypress(paddle_b_down, "Down")   # when user presses 'down' arrow call the function paddle_b_down

# main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("Pong Sound.mp4", winsound.SND_ASYNC)

    # Bottom border
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("Pong Sound.mp4", winsound.SND_ASYNC)

    # Right border
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Left border
    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("Pong Sound.mp4", winsound.SND_ASYNC)

    elif ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("Pong Sound.mp4", winsound.SND_ASYNC)
