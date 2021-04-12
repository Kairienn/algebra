# 1
import numpy as np
import matplotlib as plt
import math
def polar2cart(r,phi):
    x = r*math.cos(phi)
    y = r*math.sin(phi)
    return x,y

polar2cart(2,45)

# 2
phi = np.arange(0., 2., 1./180.)*np.pi

plt.polar(phi, [10]*len(phi))

plt.show()

# 3
phi = np.arange(0., 2., 1./180.)*np.pi

plt.polar(phi, [10]*len(phi))

plt.show()
