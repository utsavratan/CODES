import cv2
import turtle
import numpy as np
from matplotlib import pyplot as plt

def find_closest(p):
    if len(positions) > 0:
        nodes = np.array(positions)
        distances = np.sum((nodes - p) ** 2, axis=1)
        i_min = np.argmin(distances)
        return positions[i_min]
    else:
        return None

def outline():
    src_image = cv2.imread(image, 0)
    blurred = cv2.GaussianBlur(src_image, (7, 7), 0)
    th3 = cv2.adaptiveThreshold(blurred, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                thresholdType=cv2.THRESH_BINARY, blockSize=9, C=2)
    return th3

def interpolate_move(turtle_obj, start, end, steps):
    # Linearly interpolate between start and end positions
    for i in range(steps):
        intermediate_x = start[0] + (end[0] - start[0]) * (i / steps)
        intermediate_y = start[1] + (end[1] - start[1]) * (i / steps)
        turtle_obj.goto(intermediate_x, intermediate_y)
        turtle.update()

image = '1.jpg'
im = cv2.imread(image, 0)
th3 = outline()

plt.imshow(th3)
plt.axis('off')
plt.tight_layout()

WIDTH = im.shape[1]
HEIGHT = im.shape[0]

CUTOFF_LEN = ((WIDTH + HEIGHT) / 2) / 60  # 60 threshold value
iH, iW = np.where(th3 == [0])
iW = iW - WIDTH / 2
iH = -1 * (iH - HEIGHT / 2)
positions = [list(iwh) for iwh in zip(iW, iH)]

t = turtle.Turtle()
t.color("brown")
t.shapesize(1)
t.pencolor("gray30")

# Max speed
t.speed(0)
turtle.tracer(0, 0)  # Disable automatic updates

t.penup()
t.goto(positions[0])
t.pendown()

p = positions[0]
iteration = 0

# Main loop for moving the turtle
while p:
    p = find_closest(p)
    if p:
        current_pos = np.asarray(t.pos())
        new_pos = np.asarray(p)
        length = np.linalg.norm(new_pos - current_pos)
        
        if length < CUTOFF_LEN:
            interpolate_move(t, current_pos, new_pos, steps=10)  # Smoother transition
        else:
            t.penup()
            t.goto(p)
            t.pendown()

        positions.remove(p)

        # Update the turtle screen every 50 iterations
        if iteration % 500 == 0:
            turtle.update()

        iteration += 1
    else:
        p = None

turtle.update()  # Final update to ensure everything is drawn
turtle.done()