import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=275)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        super().write(arg=f"Score : {self.score}",move=False,align="center",font=("Arial", 15, "normal"),)
        
    def game_over(self):
        self.clear()
        super().write(arg=f"Game Over : {self.score}",move=False,align="center",font=("Arial", 15, "normal"),)

    def score_increased(self):
        self.score += 1
        self.clear()
        self.update_score()
