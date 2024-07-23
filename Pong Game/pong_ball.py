import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.shape("circle")
        self.ball_speed = 0.1
        self.penup()
        self.color("white")

    def move_ball(self):
        x_position = self.xcor() + self.x_move
        y_position = self.ycor() + self.y_move
        self.goto(x_position, y_position)

    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.ball_speed = 0.1
        self.goto(0,0)
        self.bounce_x()