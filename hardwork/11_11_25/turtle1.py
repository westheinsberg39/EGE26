from turtle import *
screensize(3000,3000)
m = 15
tracer(0)
pd()

for i in range(9):
    fd(30 * m)
    rt(90)
    fd(12 * m)
    rt(90)
up()
lt(270)
fd(5 * m)
lt(90)
pd()
for z in range(2):
    fd(24 * m)
    rt(90)
    fd(28 * m)
    rt(90)

up()

for x in range(-20,40):
    for y in range(-20,40):
        goto(x * m, y * m)
        dot(3,'red')

update()
done()
#25