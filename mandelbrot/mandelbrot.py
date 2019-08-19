import numpy as np
import matplotlib.pyplot as plt


# counts the number of iterations until the function diverges or
# returns the iteration threshold that we check until
def count_iterations_until_divergent(c, threshold):
    z = complex(0, 0)
    for iteration in range(threshold):
        z = (z*z) + c

        if abs(z) > 4:
            break
            pass
        pass
    return iteration


# takes the iteration limit before declaring function as convergent and
# takes the density of the atlas
# create atlas, plot mandelbrot set, display set
def mandelbrot(threshold, density):
    # location and size of the atlas rectangle
    # realAxis = np.linspace(-2.25, 0.75, density)
    # imaginaryAxis = np.linspace(-1.5, 1.5, density)
    realAxis = np.linspace(-0.22, -0.219, 20000)
    imaginaryAxis = np.linspace(-0.70, -0.699, 20000)
    # realAxis = np.linspace(1, -2, 1000)
    # imaginaryAxis = np.linspace(1, -1, 1000)
    realAxisLen = len(realAxis)
    imaginaryAxisLen = len(imaginaryAxis)

    # 2-D array to represent mandelbrot atlas
    atlas = np.empty((realAxisLen, imaginaryAxisLen))

    # color each point in the atlas depending on the iteration count
    for ix in range(realAxisLen):
        for iy in range(imaginaryAxisLen):
            cx = realAxis[ix]
            cy = imaginaryAxis[iy]
            c = complex(cx, cy)

            atlas[ix, iy] = count_iterations_until_divergent(c, threshold)
            pass
        pass

    # plot and display mandelbrot set
    plt.imshow(atlas.T, interpolation="nearest")
    plt.show()


# time to party!!
mandelbrot(120, 1000)
