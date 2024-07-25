import turtle
import time
from crossing_Player import Player
from crossing_moving_cars import Cars
from scoreBoard import Level

screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Python Turtle Graphic")
screen.tracer(0)

player = Player()
cars = Cars()
score = Level()

screen.listen()
screen.onkey(key="Up", fun=player.move)


is_game_on = True
while is_game_on:
    time.sleep(cars.car_speed)
    screen.update()
    cars.create_car()
    cars.car_move()
        
        
    # Collision with wall
    if player.ycor() > 280:
        player.back_to_position()
        score.level_increased()
        cars.speed_increased()

    # Collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            is_game_on = False

screen.exitonclick()