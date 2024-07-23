import turtle
import time
from snake_move import Snake
from snake_food import Food
from snake_score import Score

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("Black")
screen.title("Welcome to Snake Game!")

screen.tracer(0)
        


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.move_upwards)
screen.onkey(key="Down", fun=snake.move_downwards)
screen.onkey(key="Right", fun=snake.move_right)
screen.onkey(key="Left", fun=snake.move_left)

while snake.is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # Detect the food collision 
    if snake.all_snakes[0].distance(food) < 15:
        score.score_increased()
        snake.extend_snake()
        food.refresh()
        
    #Detect the wall colision
    if snake.all_snakes[0].xcor() > 280 or snake.all_snakes[0].xcor() < -300 or snake.all_snakes[0].ycor() > 310  or snake.all_snakes[0].ycor() < -290:
        snake.is_game_on = False
        score.game_over()
        
    # Detect the collision with any segment
    for i in snake.all_snakes[1:]:
        if snake.all_snakes[0].distance(i) < 10:
            snake.is_game_on = False
            score.game_over()
        
screen.exitonclick()
