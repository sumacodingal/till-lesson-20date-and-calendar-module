import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(400,400)
polygon=turtle.Turtle()
numsides=6
sidelength=70
angle=360.0/numsides
polygon.color("yellow") 
polygon.pensize(10)  # Sets pen thickness to 3 pixels
for i in range(numsides):
    polygon.forward(sidelength)
    polygon.right(angle)
turtle.done()   

 