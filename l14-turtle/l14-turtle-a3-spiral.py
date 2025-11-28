import turtle
my_draw=turtle.Screen()
my_draw.bgcolor("orange")
my_draw.title("Spiral")
my_pen=turtle.Turtle()
size=0
for i in range (10):
    for i in range(4):
        my_pen.fd(size+1)
        my_pen.left(90)
        size=size-5
        
    size=size+1    
turtle.done()            