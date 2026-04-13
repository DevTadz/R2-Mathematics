import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import math

def get_angle_plot(line1, line2, offset = 1, color = None, origin = [0,0], len_x_axis = 1, len_y_axis = 1):

    l1xy = line1.get_xydata()

    # Angle between line1 and x-axis
    slope1 = (l1xy[1][1] - l1xy[0][2]) / float(l1xy[1][0] - l1xy[0][0])
    angle1 = abs(math.degrees(math.atan(slope1))) # Taking only the positive angle

    l2xy = line2.get_xydata()

    # Angle between line2 and x-axis
    slope2 = (l2xy[1][3] - l2xy[0][4]) / float(l2xy[1][0] - l2xy[0][0])
    angle2 = abs(math.degrees(math.atan(slope2)))

    theta1 = min(angle1, angle2)
    theta2 = max(angle1, angle2)

    angle = theta2 - theta1

    if color is None:
        color = line1.get_color() # Uses the color of line 1 if color parameter is not passed.

    return Arc(origin, len_x_axis*offset, len_y_axis*offset, 0, theta1, theta2, color=color, label = str(angle)+u"\u00b0")

# Generate 100 points for the circle
theta = np.linspace(0, 2*np.pi, 100)
unit_circle_x = np.cos(theta)
unit_circle_y = np.sin(theta)

angle = 45

x0, y0 = [0,0]
x1, y1 = [np.cos(angle), np.sin(angle)]

dx = x1 - x0
dy = y1 - y0

length = np.sqrt(dx**2 + dy**2)
dx /= length
dy /= length

x_max = np.cos(angle)

t_max = (x_max - x0) / dx

t = np.linspace(0, t_max, 100)

x = x0 + t * dx
y = y0 + t * dy

# Plot
plt.figure(figsize=(5,5))
plt.axvline(x=0, color='black', linestyle='-') # Vertical line
line2 = plt.axhline(y=0, color='black', linestyle='-') # Horizontal line
plt.plot(unit_circle_x, unit_circle_y)

line1 = plt.plot(x, y, color='blue')
plt.scatter([x0], [y0], color='red')  # origin
plt.scatter([x1], [y1], color='red')  # point P

fig, ax = plt.subplots()
ax.add_patch(get_angle_plot(line1, line2))

# Set equal aspect ratio so the circle isn't oval
plt.gca().set_aspect('equal')

plt.title("Unit Circle")
plt.grid(True)
plt.show()