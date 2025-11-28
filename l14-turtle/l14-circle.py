import turtle

try:
    # your turtle drawing code
    turtle.forward(100)
    turtle.circle(50)
    
except turtle.Terminator:
    print("Turtle window closed. Exiting cleanly.")
