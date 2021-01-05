from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.draw_frame()
        self.goto(0, 260)
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def draw_frame(self):
        self.width(2)
        self.goto(-290, -290)
        self.seth(0)
        self.pd()
        for _ in range(4):
            self.fd(580)
            self.left(90)
        self.pu()
        self.width(1)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", move=False, align=ALIGNMENT, font=FONT)
