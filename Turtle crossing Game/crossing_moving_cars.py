import turtle
import random

car_colors = ["Blue", "Black", "Brown", "Purple", "Yellow", "Green", "Orange"]

class Cars:

    def __init__(self):
        self.car_speed = 0.1
        self.all_cars = []

    def create_car(self):
        random.chance = random.randint(1 ,6)
        if random.chance == 1:
            new_car = turtle.Turtle("square")
            new_car.penup()
            new_car.color(random.choice(car_colors))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_axis = random.randint(-250, 250)
            new_car.goto(300, y_axis)
            self.all_cars.append(new_car)


    def car_move(self):
        for car in self.all_cars:
            car.backward(5)
            
    def speed_increased(self):
        self.car_speed *= 0.5