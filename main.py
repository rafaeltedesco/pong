import turtle
import random

wn = turtle.Screen()
wn.bgcolor('black')
SIZE = WIDTH, HEIGHT = 800, 600
wn.setup(*SIZE)
wn.tracer(0)

score1 = 0
score2 = 0

#Player A

player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape('square')
player_a.color('white')
player_a.penup()
player_a.goto(-350, 0)
player_a.shapesize(stretch_wid=5, stretch_len=1)

#Player b
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape('square')
player_b.color('white')
player_b.penup()
player_b.goto(350, 0)
player_b.shapesize(stretch_wid=5, stretch_len=1)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx, ball.dy = 0.5, 0.5


#Line
div = turtle.Turtle()
div.color('white')
div.pensize(2)
div.goto(0, 400)
div.goto(0, -400)
div.hideturtle()

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'Player A: {score1}\t\tPlayer B:{score2}', align='center', font=('Courier', 25, 'normal'))



def player_up():
  y = player_a.ycor()
  y += 20
  player_a.sety(y)

def player_down():
  y = player_a.ycor()
  y -= 20
  player_a.sety(y)


def player_b_up():
  y = player_b.ycor()
  y += 20
  player_b.sety(y)

def player_b_down():
  y = player_b.ycor()
  y -= 20
  player_b.sety(y)

def update_score():
  pen.clear()
  pen.write(f'Player A: {score1}\t\tPlayer B:{score2}', align='center', font=('Courier', 25, 'normal'))
  


wn.listen()
wn.onkeypress(player_up, 'w')
wn.onkeypress(player_down, 's')
wn.onkeypress(player_b_up, 'Up')
wn.onkeypress(player_b_down, 'Down')


while True:
  wn.update()  
  
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  if ball.ycor() > 290 or ball.ycor() < -290:
    ball.dy *= -1
  if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= random.choice([1, -1])
    ball.dy *= random.choice([1, -1])
    score1 += 1
    update_score()
  elif ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= random.choice([1, -1])
    ball.dy *= random.choice([1, -1])
    score2 += 1
    update_score()


  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_b.ycor() +50) and (ball.ycor() > player_b.ycor() - 50):
    ball.dx *= -1

  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_a.ycor() + 50) and (ball.ycor() > player_a.ycor() - 50):
    ball.dx *= -1