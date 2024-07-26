import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Score.txt") as file:
            self.highest_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=275)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score} Highest Score : {self.highest_score}",move=False,align="center",font=("Arial", 15, "normal"),)

    def score_increased(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("Score.txt", mode = "w") as file:
                file.write(f"{self.highest_score}")
        self.score = 0
        self.update_score()

