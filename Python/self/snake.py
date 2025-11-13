#modules
import turtle
import time
import random



#variable
keypress_delay = 0.05
cd = 0
delay = 0.1
score = 0
highscore = 0



#setup
#window
window = turtle.Screen()
window.title("snake")
window.setup(width=600, height=600)
window.bgcolor("green")
window.tracer(0) 

#snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

#food
food = turtle.Turtle()
food.shape("circle")
food.speed = 0
food.color("red")
food.penup()
food.goto(0,100)

#text
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

segments = []



#functions
def up():
    if snake.direction !="down" and cd == 0:
        snake.direction = "up"
        cd = 1
        time.sleep(keypress_delay)
        cd = 0
def down():
    if snake.direction !="up" and cd == 0:
        snake.direction = "down" 
        cd = 1
        time.sleep(keypress_delay)
        cd = 0
def left():
    if snake.direction !="right" and cd == 0:
        snake.direction = "left"
        cd = 1
        time.sleep(keypress_delay)
        cd = 0
def right():
    if snake.direction !="left" and cd == 0:
        snake.direction = "right"
        cd = 1
        time.sleep(keypress_delay)
        cd = 0
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)
def add_segment():
    segment = turtle.Turtle()
    segment.shape("square")
    segment.speed(0)
    segment.color("dark grey")
    segment.penup()
    segments.append(segment)


#keyboard
window.listen()
window.onkeypress(up, "w")
window.onkeypress(down, "s")
window.onkeypress(left, "a")
window.onkeypress(right, "d")

#main
while True:
    window.update()

    if snake.xcor() > 290 or snake.xcor() <-290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        if highscore < score:
            highscore = score

        score = 0
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highscore), align="center", font=("Courier", 24, "normal")) 

    if snake.distance(food) < 17:
        x = random.randint(-285, 285)
        y = random.randint(-285, 285)
        food.goto(x,y) 

        add_segment()

        if delay != 0:
            delay = delay - 0.001
        score += 10

        if score > highscore:
            highscore = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highscore), align="center", font=("Courier", 24, "normal")) 

    for seg in range(len(segments)-1,0,-1):
        x = segments[seg-1].xcor()
        y = segments[seg-1].ycor()
        segments[seg].goto(x, y)

    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)

    move()
    time.sleep(delay)


window.mainloop()