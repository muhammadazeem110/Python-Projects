import turtle
import random

class Food(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh()
        
    def refresh(self):
        self.goto(random.randint(-270,270), random.randint(-260,260))
        
        
