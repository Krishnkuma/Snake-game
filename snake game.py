import turtle as t
import random
import time

t.bgcolor('yellow')

caterpillar=t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf=t.Turtle()
leaf.shape('circle')
leaf.color('green')
leaf.speed(0)
leaf.penup()
leaf.hideturtle()

score_turtle=t.Turtle()
score_turtle.speed(0)
score_turtle.hideturtle()

game_started=False
text_turtle=t.Turtle()
text_turtle.write('press space to start',align='center',font=('Arial',16,'bold'))
text_turtle.hideturtle()

def outside():
    top=(t.window_height()/2)-35
    bottom=(-t.window_height()/2)-35
    left=(-t.window_width()/2)-35
    right=(t.window_width()/2)-35
    (x,y)=caterpillar.pos()
    outside=x<left or x>right or y>top or y<bottom
    return outside

def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('game over',align='center',font=('arial',16,'bold'))

def leaf_pos():
    leaf.hideturtle()
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    leaf.goto(x,y)
    leaf.st()

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    y=(t.window_height()/2)-50
    x=(t.window_width()/2)-50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))


def start_game():
    global game_started
    if game_started:
        return
    game_started=True

    score=0
    text_turtle.clear()
    caterpillar_speed=2
    caterpillar_length=3
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.st()
    display_score(score)
    leaf_pos()
    while True:
        caterpillar.fd(caterpillar_speed)
        if caterpillar.distance(leaf)<20:
            leaf_pos()
            caterpillar_length=caterpillar_length+1
            caterpillar.shapesize(1,caterpillar_length,1)
            caterpillar_speed=caterpillar_speed+0.1
            score=score+10
            display_score(score)
        if outside():
            game_over()
            break

def move_up():
    if caterpillar.heading()==0 or caterpillar.heading()==180:
        caterpillar.setheading(90)
def move_down():
    if caterpillar.heading()==0 or caterpillar.heading()==180:
        caterpillar.setheading(270)
def move_left():
    if caterpillar.heading()==90 or caterpillar.heading()==270:
        caterpillar.setheading(180)
def move_right():
    if caterpillar.heading()==90 or caterpillar.heading()==270:
        caterpillar.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.onkey(move_right,'Right')
t.listen()
t.mainloop()
time.sleep(3)