import turtle
import winsound

window= turtle.Screen()
window.title("Pong by Madda")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) #stops the window from updating-speedup tips

#paddle A declaration 
paddle_a=turtle.Turtle()
paddle_a.speed(0) #speed of animation- sets for max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)#left side center

#paddle B declaration
paddle_b=turtle.Turtle()
paddle_b.speed(0) #speed of animation- sets for max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)#right side center

#ball declaration
ball=turtle.Turtle()
ball.speed(0) #speed of animation- sets for max
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)#center
ball.dx=0.2 #move by 0.1 pixels to right
ball.dy=-0.2 #move by 0.1 pixels to top

#calculate the score
score_a=0
score_b=0


#display the score pattern
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier",24,"normal"))


#functions to move the paddles

# 1. paddle a-up movements
def paddle_a_up():
    y=paddle_a.ycor() #go up on the screen
    y+=20 #add 20pixels to y co-ordinates
    paddle_a.sety(y)

# 2. paddle a-down movements
def paddle_a_down():
    y=paddle_a.ycor() #go down on the screen
    y-=20 #sub 20pixels to y co-ordinates
    paddle_a.sety(y)

# 3. paddle b-up movements
def paddle_b_up():
    y=paddle_b.ycor() #go up on the screen
    y+=20 #add 20pixels to y co-ordinates
    paddle_b.sety(y)

# 4. paddle b-down movements
def paddle_b_down():
    y=paddle_b.ycor() #go down on the screen
    y-=20 #sub 20pixels to y co-ordinates
    paddle_b.sety(y)


#keyboard binding
window.listen() #listen to keyboard input
window.onkeypress(paddle_a_up, "q") # when user presses q
window.onkeypress(paddle_a_down, "w") # when user presses w
window.onkeypress(paddle_b_up, "p") # when user presses p
window.onkeypress(paddle_b_down, "o") # when user presses o

#main game loop
while True:
    window.update() #update the screen everytime it runs
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor()>290: #top
        ball.sety(290)
        ball.dy*= -1 #reverse the direction
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    elif ball.ycor()< -290: #bottom
        ball.sety(-290)
        ball.dy*= -1 #reverse the direction
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.xcor()>390: #right sides
        ball.goto(0,0)
        ball.dx *=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))

    elif ball.xcor()<-390: #left sides
        ball.goto(0,0)
        ball.dx *=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))

    #right paddle & ball collisions
    if (ball.xcor() > 340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

     #left paddle & ball collisions
    elif (ball.xcor() <-340 and ball.xcor() >-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

  