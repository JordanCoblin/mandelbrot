import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import cmath

# x -> x^2
# mandelbrot -> z -> z^2 + a
# 100 iterations, if greater than 1000, not in set

bro_set = []
bro_set_cols = []

real = np.arange(-2, .5, .002)
imag = np.arange(-1.25,  1.25, .002)

def mandelbrot(a):
	max_iterations = 100

	z = 0
	for i in range(0,max_iterations):
		z = pow(z, 2) + a
		if abs(z) > 2: 
			return i

	return max_iterations

points = np.zeros((len(real), len(imag)))
for i, num_real in enumerate(real):
	for j, num_imag in enumerate(imag):
		points[i, j] = mandelbrot(complex(num_real, num_imag))

# faves = gist_yarg, afmhot, gist_earth, jet, nipy_spectral
plt.imshow(points.T, cmap='gist_yarg', extent=[-2, .5, -1.25, 1.25])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()