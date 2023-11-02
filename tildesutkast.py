import turtle

def skapa_padda(färg):
    t = turtle.Turtle()
    t.shape('turtle')
    t.speed(0)
    t.color(färg)
    return t

def rektangel(bredd, längd, färg):
    t = skapa_padda(färg)
    t.fillcolor(färg)
    t.begin_fill()
    for dist in (bredd, längd, bredd, längd):
        t.forward(dist)
        t.left(90)
    t.end_fill()

def kvadrat(längd, färg):
    t = skapa_padda(färg)
    t.fillcolor(färg)
    t.begin_fill()
    for x in range(4):
        t.forward(längd)
        t.right(90)
    t.end_fill()

def stjöärna2(längd, färg):
    t = skapa_padda(färg)
    t.fillcolor(färg)
    t.begin_fill()
    for x in range(5):
        t.forward(längd)
        t.right(144)
    t.end_fill()

def stjärna(längd, färg):
    t = skapa_padda(färg)
    t.fillcolor(färg)
    t.begin_fill()
    for dist in (längd, längd, längd, längd, längd):
        t.forward(dist)
        t.right(144)
    t.end_fill()

t = skapa_padda('blue')
t.fillcolor()
t.begin_fill()
for x in range(5):
    t.forward(100)
    t.right(144)
t.end_fill()





input()