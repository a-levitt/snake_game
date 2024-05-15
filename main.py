from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("olive")
screen.title("Snake game")

start_positions = [(0, 0), (-20, 0), (-40, 0)]


for position in start_positions:
    segment = Turtle(shape="square")
    segment.penup()
    segment.color("darkgreen")
    segment.goto(position)








screen.exitonclick()