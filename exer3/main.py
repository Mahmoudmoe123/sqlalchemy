import numpy as x

randomnumbers = x.random.rand(10)
mean = x.mean(randomnumbers)
median = x.median(randomnumbers)
stand = x.std(randomnumbers)

print("Random numbers: ", randomnumbers)
print("Mean: ", mean)
print("Median: ", median)
print("Standard Deviation: ", stand)
