from turtle import  *
#we want to paint a house
shape("triangle")
#step1: draw a square
speed(7)

width(7)
color("pink")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90) 
end_fill()
#end of square

#drawing a door
forward(70)
color("light blue")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#drawing a roof
penup()
goto(200, 200)
pendown()

color("light blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#we want to draw a window
color("pink")
left(30)
forward(60)

color("light blue")
begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

end_fill()

#another window
color("pink")
forward(140)
left(90)
forward(200)
left(90)
forward(140)

color("light blue")
begin_fill()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


exitonclick()