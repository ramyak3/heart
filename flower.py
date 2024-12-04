import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("purple")
pen.speed(10)

# Draw flower with turtle
def draw_petal():
    pen.color("pink")
    pen.circle(100, 60)  # Draw a petal
    pen.left(120)
    pen.circle(100, 60)  # Draw the other side of the petal
    pen.left(120)

# Draw the full flower
for _ in range(6):
    draw_petal()
    pen.left(60)

# Draw the center of the flower
pen.penup()
pen.goto(0, -20)
pen.pendown()
pen.color("yellow")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

# Draw some text
pen.penup()
pen.goto(0, -150)
pen.pendown()
pen.color("purple")
pen.write("A Beautiful Flower", align="center", font=("Arial", 24, "bold"))

# Hide turtle and finish
pen.hideturtle()
turtle.done()
