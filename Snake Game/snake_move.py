import turtle

starting_postion = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.new_heading = 0
        self.is_game_on = True
        self.direction = "Right"

    def create_snake(self):
        for position in starting_postion:
            self.add_segment(position)
            
    def add_segment(self, position):
        new_snake = turtle.Turtle("square")
        new_snake.speed("fastest")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.all_snakes.append(new_snake)
        
    def extend_snake(self):
        self.add_segment(self.all_snakes[-1].position())
    
    def move_snake(self):
        for i in range(len(self.all_snakes) - 1, 0, -1):
            x_axis = self.all_snakes[i - 1].xcor()
            y_axis = self.all_snakes[i - 1].ycor()
            self.all_snakes[i].goto(x_axis, y_axis)
        self.all_snakes[0].setheading(self.new_heading)
        self.all_snakes[0].forward(20)  

    def move_upwards(self):
        if self.new_heading != 270:
            self.new_heading = 90

    def move_downwards(self):
        if self.new_heading != 90:
            self.new_heading = 270

    def move_left(self):
        if self.new_heading != 0:
            self.new_heading = 180

    def move_right(self):
        if self.new_heading != 180:
            self.new_heading = 0
