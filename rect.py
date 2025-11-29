import turtle
screen = turtle.Screen()
screen.title("Draw a Closed Rectangle")
pen = turtle.Turtle()
def draw_rectangle(width, height):
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height) 
        pen.right(90)
rectangle_width = 200
rectangle_height = 100
draw_rectangle(rectangle_width, rectangle_height)
turtle.done()