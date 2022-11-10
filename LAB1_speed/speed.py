import numpy
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
media = [32,111,138,28,59,77,97]
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.median(speed)
y = stats.mode(speed, keepdims = True)
z = numpy.std(speed)
w = numpy.median(media)
a = numpy.percentile(ages, 75)
m = numpy.random.uniform(0.0, 5.0, 250)
print(x)
print(y)
print(z)
print(a)
print(m)

