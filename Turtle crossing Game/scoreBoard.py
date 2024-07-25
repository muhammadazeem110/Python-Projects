import turtle

class Level(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.level = 0
        self.hideturtle()
        self.update_level()
        
    def update_level(self):
        self.clear()
        self.goto(-285 , 260)
        self.write(arg=f"Level : {self.level}", move=False, align='left', font=('Courier', 17, 'normal'))
        
    def level_increased(self):
        self.level +=1
        self.update_level()
        
    def game_over(self):
        self.goto(-90,0)
        self.write(arg="Game Over", move=False, align='left', font=('Courier', 24, 'normal'))