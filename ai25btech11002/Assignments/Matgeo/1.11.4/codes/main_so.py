import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from line.funcs import line_gen 

lib = ctypes.CDLL("./libmag.so")
lib.mag.argtypes = [ctypes.c_int, ctypes.c_double,
                    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),
                    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS")]
lib.mag.restype = ctypes.c_double

A = np.array([-2, -1, 2], dtype=np.double)

# Desired magnitude for B
M = 9.0
B = np.zeros_like(A)

lib.mag(A.size, M, A, B)

# Origin
O = np.array([0, 0, 0], dtype=np.double)

# Plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

x_OA = line_gen(O, A)
x_OB = line_gen(O, B)

ax.plot(x_OA[0,:], x_OA[1,:], x_OA[2,:], color='pink', label='OA')
ax.plot(x_OB[0,:], x_OB[1,:], x_OB[2,:], color='y', label='OB')

ax.scatter(*A, color='r', s=100, label=f'A {tuple(A)}')
ax.scatter(*B, color='g', s=100, label=f'B (|B|={M})')
ax.scatter(*O, color='b', s=100, label='O')

ax.text(*A, ' A', color='r')
ax.text(*B, ' B', color='g')
ax.text(*O, ' O', color='b')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title(f"A vector B of magnitude {M} in direction of A")
ax.legend()
ax.grid(True)

plt.savefig("../Figs/plot.png")
plt.show()
