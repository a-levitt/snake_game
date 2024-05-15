from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("olive")
screen.title("Snake game")
screen.tracer(0) #no animation

snake = Snake()

game_loop = True
while game_loop:
    screen.update()
    time.sleep(0.1)
    snake.move()




screen.exitonclick()