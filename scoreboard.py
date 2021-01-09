from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Arial", 16, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file="data.txt", mode='r') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.draw_frame()
        self.goto(0, 260)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

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

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", move=False, align=ALIGNMENT, font=FONT)

    def countdown(self):
        self.update_score()
        self.goto(0, 0)
        self.write(arg=f"GET READY", move=False, align=ALIGNMENT, font=FONT)
        time.sleep(1)
        for num in range(3, 0, -1):
            self.update_score()
            self.goto(0, 0)
            self.write(arg=f"{num}", move=False, align=ALIGNMENT, font=FONT)
            time.sleep(1)
        self.update_score()

