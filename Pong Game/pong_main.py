import turtle
import time
from pong_paddles import Paddles
from pong_ball import Ball
from pong_score import Score

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Welcome to paddle!")

r_paddle = Paddles(378)
l_paddle = Paddles(-386)
ball = Ball()
score = Score() 
score.update_score()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_upward)
screen.onkey(key="Down", fun=r_paddle.move_downward)
screen.onkey(key="w", fun=l_paddle.move_upward)
screen.onkey(key="s", fun=l_paddle.move_downward)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move_ball()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 350) or (ball.distance(l_paddle) < 50 and ball.xcor() < -350):
        ball.bounce_x()
        
    #Dectect out the ball from the screen    
    if ball.xcor() > 378:
        ball.reset_position()
        score.left_point()
        score.update_score()
        
    if ball.xcor() < -386:
        ball.reset_position()
        score.right_point()
        score.update_score()
        

screen.exitonclick()
