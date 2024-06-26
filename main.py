from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("olive")
screen.title("Snake game")
screen.tracer(0) #no animation

scoreboard = ScoreBoard()
snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_loop = True
while game_loop:
    screen.update()
    time.sleep(snake.snake_speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        time.sleep(snake.increase_speed())
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_loop = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_loop = False
            scoreboard.game_over()

screen.exitonclick()