import turtle as tur
import colorsys as cs

tur.setup(800,800)
tur.speed(10)
tur.tracer(10)
tur.width(2)
tur.bgcolor('black')
r = 10
for j in range(25):
    for i in range(15):
        for q in range(100):
            tur.color(cs.hsv_to_rgb(i/15, j/25, True))
            tur.right(90)
            tur.circle(200-j*4,90)
            tur.left(90)
            tur.circle(200-j*4,90)
            tur.right(100)
            tur.circle(q + r,24)
tur.hideturtle()
tur.done