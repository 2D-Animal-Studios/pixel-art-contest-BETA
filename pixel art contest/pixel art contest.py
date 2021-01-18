import turtle
import time
from random import *
import pygame
pygame.init()
print("controls: to chose winners 1 for red 2 for blue")
print("to chose a subject press 0")
print("wasd: move player 1(red) 7 and 4: turn drawing on and off for player 1")
print("arrow keys: move player 2(blue) 9 and 6: turn drawing on and off for player 2")

items = ["dog", "doll", "crayon", "sign", "town", "car", "house", "kid", "pen", "shirt"]
wn = turtle.Screen()
wn.title("pixel art contest")
wn.setup(width=800, height=600)

red2 = 0
blue2 = 0

p1 = turtle.Turtle()
p1.hideturtle()
p1.shape("circle")
p1.penup()
p1.goto(-150, 0)
p1.color("red")


p2 = turtle.Turtle()
p2.hideturtle()
p2.shape("circle")
p2.penup()
p2.goto(150, 0)
p2.color("cyan")

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("red: 0   blue: 0", align="center", font=("Courier", 24, "normal"))

line = turtle.Turtle()
line.hideturtle()
line.penup()
line.goto(0, -500)
line.pendown()
line.goto(0, 500)


p1.showturtle()
p2.showturtle()

pygame.mixer.music.load('pixel burst.wav')
pygame.mixer.music.play(-1)


def up():
    y = p1.ycor()
    y += 10
    p1.sety(y)


def down():
    y = p1.ycor()
    y -= 10
    p1.sety(y)


def left():
    x = p1.xcor()
    x -= 10
    p1.setx(x)


def right():
    x = p1.xcor()
    x += 10
    p1.setx(x)


def pup():
    y = p2.ycor()
    y += 10
    p2.sety(y)


def pdown():
    y = p2.ycor()
    y -= 10
    p2.sety(y)


def pleft():
    x = p2.xcor()
    x -= 10
    p2.setx(x)


def pright():
    x = p2.xcor()
    x += 10
    p2.setx(x)


def win1():
    global red2
    red2 += 1
    pen.clear()
    pen.write("red: {}   blue: {}".format(red2, blue2), align="center", font=("Courier", 24, "normal"))
    wn.bgcolor("red")
    p1.color("white")
    time.sleep(3)
    wn.bgcolor("white")
    p1.color("red")
    p1.penup()
    p1.clear()
    p1.goto(-150, 0)
    p2.penup()
    p2.clear()
    p2.goto(150, 0)


def win2():
    global blue2
    blue2 += 1
    pen.clear()
    pen.write("red: {}   blue: {}".format(red2, blue2), align="center", font=("Courier", 24, "normal"))
    wn.bgcolor("cyan")
    p2.color("white")
    time.sleep(3)
    wn.bgcolor("white")
    p2.color("cyan")
    p1.penup()
    p1.clear()
    p1.goto(-150, 0)
    p2.penup()
    p2.clear()
    p2.goto(150, 0)


def pu():
    p1.penup()


def pd():
    p1.pendown()


def pu2():
    p2.penup()


def pd2():
    p2.pendown()


def subis():
    sub = choice(items)
    print("The subject is", sub)


wn.listen()
wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")
wn.onkeypress(win1, "1")
wn.onkeypress(win2, "2")
wn.onkeypress(pup, "Up")
wn.onkeypress(pdown, "Down")
wn.onkeypress(pleft, "Left")
wn.onkeypress(pright, "Right")
wn.onkeypress(pu, "7")
wn.onkeypress(pd, "4")
wn.onkeypress(pu2, "9")
wn.onkeypress(pd2, "6")
wn.onkeypress(subis, "0")
while True:
    wn.update()
    if p2.xcor() < 10:
        p2.goto(10, 0)
    if p1.xcor() > -10:
        p1.goto(-10, 0)