import turtle

class Player(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.speed("fastest")
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.y_position = -280
        self.goto(0, self.y_position)
        
    def move(self):
        self.forward(20)
        
    def back_to_position(self):
        self.goto(0, self.y_position)