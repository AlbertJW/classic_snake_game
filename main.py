from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()

    screen.onkey(fun=snake.up, key='Up')
    screen.onkey(fun=snake.down, key='Down')
    screen.onkey(fun=snake.left, key='Left')
    screen.onkey(fun=snake.right, key='Right')

    game_on = True

    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #  Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        s_x = snake.head.xcor()
        s_y = snake.head.ycor()
        if s_x > 285 or s_x < -285 or s_y > 285 or s_y < -285:
            game_on = False
            scoreboard.game_over()

        #  Detect tail collision
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                scoreboard.game_over()

    screen.exitonclick()
