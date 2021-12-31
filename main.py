from turtle import Screen  # this imports the Screen method from the turtle module
from snake import Snake  # this imports the Snake class from the snake object.
from food import Food  # this imports the Food class from the created food object.
from scoreboard import Scoreboard  # this imports the Scoreboard class from the created scoreboard object.
import time  # this imports the time module

screen = Screen()  # creating a Screen object that class the screen class from Turtle
screen.setup(width=600, height=600)  # Defining the Screen size, width and height
screen.bgcolor("black")  # Defining the background color of the screen
screen.title("My Snake Game")  # The title of the game when run
screen.tracer(0)  # This will make sure the tracer or line doesnt move on screen.

snake = Snake()  # This is the Snake Class being stored within the snake object. This is so it can be called / refer.
food = Food()  # This is the Food Class being stored within the food object so that it can be called.
scoreboard = Scoreboard()  # This is the Scoreboard class being stored within the scoreboard object

screen.listen()  # This is us accessing the screen module's listening method.
screen.onkey(snake.up, "Up")  # allows us to move up
screen.onkey(snake.down, "Down")  # allows us to move down
screen.onkey(snake.left, "Left")  # allows us to move left
screen.onkey(snake.right, "Right")  # allows us to move right

game_is_on = True  # this is a boolean statement that will control our snake game.
while game_is_on:  # This is a while loop that refers to the game_is_on = True.
    screen.update()  # Constantly updating the screen for any changes.
    time.sleep(0.1)  # Constantly This is the number of seconds execution to be suspended.
    snake.move()  # This is where we are calling the move() within the snake classs.

    #Detect collision with food.
    if snake.head.distance(food) < 15:  # This is talking about the snake class with a set heading of
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()
