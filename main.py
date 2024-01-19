from turtle import *
from slider import Slider
from Ball import Ball
from walls import Wall
from ScoreBoard import Score

window = Screen()
window.setup(width=1000, height=500)
window.tracer(5)  # Set the update speed
window.title("BreakOut")
timer = 5

# Slider
paddle = Slider()

# Ball
ball = Ball()

#Wall
wall = Wall()

#ScoreBoard
score = Score()

window.listen()
window.onkey(paddle.go_right, "Right")
window.onkey(paddle.go_left, "Left")
is_on = True

def game_update():
    global is_on, timer
    if is_on:
        window.update()
        if ball.ycor() > 250:
            ball.bounce_y()

        elif ball.ycor() < -220 and ball.distance(paddle) <= 100:
            ball.bounce_y()
            print("Hit")

        elif ball.xcor() > 500 or ball.xcor() < -500:
            ball.bounce_x()

        elif ball.ycor() > 60:
            if wall.check_collision(ball):
                score.update_score()
                if not wall.get_walls():
                    is_on = False
                    ball.home()
                    ball.hideturtle()
                    ball.setpos(-280, 0)
                    ball.write("You Won", font=("Cooper Black", 80, "italic"))
                if wall.get_walls() == 20:
                    timer -= 2


        elif ball.ycor() < -260:
            is_on = False
            ball.home()
            ball.hideturtle()
            ball.setpos(-40git0, -100)
            ball.write("Game Over", font=("Cooper Black", 100, "italic"))

        ball.move()
        window.ontimer(game_update, timer)  # Adjust the time delay as needed

game_update()  # Start the game update loop
window.exitonclick()
