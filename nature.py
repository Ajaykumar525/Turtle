from turtle import *
speed(200)
# Set the background Color so that all widgets & colors are visible on screen
bgcolor("lightskyblue")

# To draw sun in the sky
up()
goto(200,200)
down()
color("yellow")
begin_fill()
circle(25)
end_fill()



#cloud 1 near to sun
up()
goto(250,250)
down()
color("white")
begin_fill()
circle(9)
end_fill()
#cloud 2 near to sun
up()
goto(240,250)
down()
color("white")
begin_fill()
circle(8)
end_fill()
#cloud 3 near to sun
up()
goto(260,250)
down()
color("white")
begin_fill()
circle(5)
end_fill()

# To draw multiple clouds starting from left to right
#cloud 1
up()
goto(-225, 195)
down()
color("white")
begin_fill()
circle(9)
end_fill()
#cloud 2
up()
goto(-215, 200)
down()
color("white")
begin_fill()
circle(12)
end_fill()
#cloud 3
up()
goto(-200, 200)
down()
color("white")
begin_fill()
circle(15)
end_fill()
#cloud 4
up()
goto(-200, 215)
down()
color("white")
begin_fill()
circle(12)
end_fill()
#cloud 5
up()
goto(-180, 200)
down()
color("white")
begin_fill()
circle(15)
end_fill()

# Drawing Left side Mountain nearer to first cloud
penup()
goto(-337, 40)
pendown()
color("dimgray")
begin_fill()
for i in range(3):
    forward(200)
    left(120)
end_fill()

# Drawing Right side Mountain nearer to Sun
penup()
goto(133, 40)
pendown()
begin_fill()
for i in range(3):
    forward(200)
    left(120)
end_fill()



#upper dark line
penup()
goto(-337, 40)
pendown()
forward(671)

#Drawing trees near Left mountain
penup()
goto(-330, 40)
pendown()
color("green")
begin_fill()
for i in range(50):
    circle(5)
    forward(10)
end_fill()

#Drawing trees near right mountain
penup()
goto(156, 40)
pendown()
color("green")
begin_fill()
for i in range(15):
    circle(7)
    forward(12)
end_fill()

# Adding Water color: mediumaquamarine
penup()
goto(-337, -5)
pendown()
color("mediumaquamarine")
begin_fill()
for i in range(2):
    forward(672)
    left(90)
    forward(43)
    left(90)
end_fill()

#Draw Simple boat
penup()
goto(-200, 10)
pendown()
color("goldenrod")
begin_fill()
forward(25)
left(120)
forward(40)
left(150)
forward(37)
end_fill()

#To show simple water line in river
penup()
goto(-195, 9)
pendown()
color("wheat")
left(90)
forward(25)

#river side border line
color("black")
penup()
goto(-337, -10)
pendown()
forward(672)

#Drawing Road
penup()
goto(-337, -50)
pendown()
color("grey")
begin_fill()
for i in range(2):
    forward(672)
    left(90)
    forward(40)
    left(90)
end_fill()

#drawing yellow line in center of road
penup()
goto(-337, -29)
pendown()
color("yellow")
forward(672)

#Railing border on river side
color("black")
penup()
goto(-337, -5)
pendown()
forward(672)

#Railing border on river side
color("rosybrown")
penup()
goto(-337, -6)
pendown()
forward(672)

#Railing border on river side
color("sandybrown")
penup()
goto(-337, -8)
pendown()
forward(672)

#planting small trees near river
penup()
goto(-330, -60)
pendown()
color("green")
begin_fill()
for i in range(67):
    circle(6)
    forward(10)
end_fill()

#Lawn
penup()
goto(-337, -60)
pendown()
color("yellowgreen")
begin_fill()
for i in range(2):
    forward(672)
    right(90)
    forward(220)
    right(90)
end_fill()


#House Code
penup()
goto(50, -200)
pendown()
pensize(3)
color("chocolate", "azure") # (stroke, fill)
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()

penup()
goto(50, -100)
pendown()
color("chocolate", "ghostwhite")
begin_fill()
for i in range(3):
    forward(100)
    left(120)
end_fill()

#For air circulation
penup()
goto(100, -70)
pendown()
pensize(2)
color("black", "lightcyan")
begin_fill()
circle(15)
end_fill()

penup()
goto(150, -100)
pendown()
pensize(3)
color("chocolate", "firebrick")
begin_fill()
forward(150)
left(120)
forward(100)
left(60)
forward(150)
end_fill()

penup()
goto(150, -200)
pendown()
pensize(3)
right(180)
color("chocolate", "azure")
begin_fill()
forward(144)
left(90)
forward(100)
left(90)
forward(143)
end_fill()


#Door
penup()
goto(200, -200)
pendown()
pensize(3)
right(90)
color("saddlebrown", "Peru") # (stroke, fill)
begin_fill()
for i in range(4):
    forward(55)
    right(90)
end_fill()



#window

penup()
goto(80, -130)
pendown()
pensize(3)
right(90)
color("chocolate","lightcyan")
begin_fill()
for i in range(4):
    forward(30)
    right(90)
end_fill()

up()
goto(95,-130)
down()
right(90)
forward(30)
color("sienna")
up()
goto(228,-146)
down()
forward(54)

#door handle
up()
goto(228,-176)
down()
circle(2)


#Bird on left side
up()
goto(-150,200)
down()
pensize(1)
color("black")
right(90)
circle(20,40)
right(90)
circle(20,40)
#Bird on right side
up()
goto(235,240)
down()
pensize(2)
color("black")
circle(20,40)
right(90)
circle(20,40)



#road from the base of house
left(30)
penup()
goto(200, -200)
pendown()
color("gray")
begin_fill()
fd(445)
left(170)
fd(400)
left(40)
fd(118)
end_fill()

#planting left side tree branch
penup()
goto(-232, -279)
pendown()
right(43)
lt(45)
color("limegreen")
begin_fill()
for i in range(8):
    circle(20,40)
    right(45)
    circle(20,40)
lt(43)
end_fill()

#planting right side tree branch
penup()
goto(180, -279)
pendown()
lt(45)
color("limegreen")
begin_fill()
for i in range(7):
    circle(20,40)
    right(45)
    circle(20,40)
fd(12)
end_fill()











done()

