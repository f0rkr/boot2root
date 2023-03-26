from turtle import *

f = open("../turtle", "r")
color('white')
begin_fill()
goto(-200,0)
r=0
b=-200
for i in f:
    i = i.split()
    if len(i)  == 0:
        b+=150
        color('white')
        left(90)
        if r==3:
            b+=80
            goto(b,100)
        else:
            goto((b,0))
        r+=1
    elif i[0] == "Avance":
        color('red')
        forward(int(i[1]))
    elif i[0] == "Recule":
        color('red')
        backward(int(i[1]))
    elif i[1] == "droite":
        color('red')
        right(int(i[3]))
    elif i[1] == "gauche":
        color('red')
        left(int(i[3]))
end_fill()
done()
f.close()
