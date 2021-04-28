from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right, "Right")

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_running = False
        scoreboard.game_over()

    # Detect collision with tail

    for i in snake.segment:
        if i == snake.head:
            pass
        elif snake.head.distance(i) < 7:
            game_running = False
            scoreboard.game_over()

screen.exitonclick()