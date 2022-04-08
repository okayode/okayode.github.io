import random
import numpy as np
import matplotlib.pyplot as plt

N = 100000

circle_points = 0
square_points = 0
inside_circle_x= [] 
inside_circle_y= [] 
outside_circle_x= [] 
outside_circle_y= [] 

for i in range(N):
    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)
    radius = rand_x**2 + rand_y**2
    
    # Checking if (x, y) lies inside the circle
    if radius<= 1:
      circle_points+= 1
      inside_circle_x.append(rand_x)
      inside_circle_y.append(rand_y)

    elif radius> 1:
      outside_circle_x.append(rand_x)
      outside_circle_y.append(rand_y)
      
    square_points+= 1
    
    # Estimating value of pi,
    # pi= 4*(no. of points generated inside the
    # circle)/ (no. of points generated inside the square)
    pi = 4* circle_points/ square_points

print("Estimation of Pi=", pi)

plt.scatter(inside_circle_x,inside_circle_y, c='b', alpha=0.5, edgecolor=None)
plt.scatter(outside_circle_x,outside_circle_y, c='r', alpha=0.5, edgecolor=None)

plt.show()
