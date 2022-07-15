import turtle
import time
import random
import winsound
delay=0.1

#Score
score=0
high_score=0


#Game Screen 
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=600,height=600)
window.tracer(0)

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake Food
Food = turtle.Turtle()
Food.speed(0)
Food.shape("circle")
Food.color("red")
Food.penup()
Food.goto(0,100)

Tail=[]

#Towrite
Towrite = turtle.Turtle()
Towrite.speed(0)
Towrite.shape("square")
Towrite.color("white")
Towrite.penup()
Towrite.hideturtle()
Towrite.goto(0,250)
Towrite.write("Score: 0  High Score: 0",align="center")

#Functions
def go_up():
    if head.direction!="down":
        head.direction = "up"

def go_down():
    if head.direction!="up":
        head.direction = "down"

def go_left():
    if head.direction!="right":
        head.direction = "left"

def go_right():
    if head.direction!="left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#Keyboard Bind
window.listen()
window.onkeypress(go_up,"w")
window.onkeypress(go_down,"s")
window.onkeypress(go_left,"a")
window.onkeypress(go_right,"d")

#Main Game


while True:
    window.update()

    #Checking For Collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        #print("GAME OVER!!!")

        #hiding the segments
        for segment in Tail:
            segment.goto(1000,1000)

        Tail.clear()
        score=0
        Towrite.clear()
        Towrite.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Century Schoolbook",20,"normal"))
        Towrite.clear()
        Towrite.write("GAME OVER!!!! Try Again---",align="center",font=("Century Schoolbook",20,"normal"))
        winsound.PlaySound("no",winsound.SND_ASYNC)

        

    if head.distance(Food)<20:
        #to move food to random place
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        Food.goto(x,y)

        #Adding new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        Tail.append(new_segment)

        #To increase the score
        score+=10
        if score>high_score:
            high_score=score

        Towrite.clear()
        Towrite.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Century Schoolbook",20,"normal"))
        winsound.PlaySound("yes",winsound.SND_ASYNC)

    #To Move The End segements first in reverse order
    for i in range(len(Tail)-1,0,-1):
        x = Tail[i-1].xcor()
        y = Tail[i-1].ycor()
        Tail[i].goto(x,y)

    #To Move segment 0 to where the Head is
    if len(Tail)>0:
        x = head.xcor()
        y = head.ycor()
        Tail[0].goto(x,y)

    move()
    
    #Checking for body-head collision
    for segment in Tail:
        if segment.distance(head) < 5:
            time.sleep(1)
            #head.goto(0,0)
            head.direction = "stop"
            print("GAME OVER!!!")
            #hiding the segments
            for segment in Tail:
                segment.goto(1000,1000)
                Tail.clear()

                score=0
                Towrite.clear()
                Towrite.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Century Schoolbook",20,"normal"))
                Towrite.clear()
                Towrite.write("GAME OVER!!!! Try Again---",align="center",font=("Century Schoolbook",20,"normal"))
                winsound.PlaySound("no",winsound.SND_ASYNC)
                

    
    

    time.sleep(delay)
window.mainloop()
'''
    '''

