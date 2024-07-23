import turtle


class Paddles(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)
        
    
    def create_paddle(self, position):
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position, 0)

    def move_upward(self):
        x_position = self.xcor()
        y_position = self.ycor()
        self.goto(x_position, y_position + 50)

    def move_downward(self):
        x_position = self.xcor()
        y_position = self.ycor()
        self.goto(x_position, y_position - 50)
