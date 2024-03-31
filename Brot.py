import matplotlib.pyplot as plt
import numpy as np
def mandelbrot(c):
    z = 0
    max_iterations = 100
    for n in range(max_iterations):
        z = z**2 + c
        if abs(z) > 2:
            return n
    return 0
def generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iterations=100):
    image = np.zeros((height, width))
    for i, x in enumerate(np.linspace(xmin, xmax, width)):
        for j, y in enumerate(np.linspace(ymin, ymax, height)):
            c = complex(x, y)
            image[j, i] = mandelbrot(c)
    return image
xmin, xmax, ymin, ymax = -2.5, 1, -1.5, 1.5
width, height = 500, 500
max_iterations = 100
image = generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iterations)
fig, ax = plt.subplots()
plt.imshow(image, cmap='hot', interpolation='nearest')
plt.axis('off')
plt.show()
