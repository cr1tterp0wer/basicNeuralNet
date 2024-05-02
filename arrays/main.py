import numpy
import matplotlib.pyplot as plt

a = numpy.zeros([3,2])
print(a)

a[0,0] = 1
a[0,1] = 2
a[1,0] = 9
a[2,1] = 12
print(a)
print(a[0,1])

v = a[1,0]
print(v)

plt.imshow(a, interpolation="nearest")
plt.show()
