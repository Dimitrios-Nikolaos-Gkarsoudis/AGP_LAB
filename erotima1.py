import random
from itertools import combinations
import utils

points = []

for i in range(100):
    points.append((random.randint(-100, 100), random.randint(-100, 100)))

for point in points:
    print(point)

print(utils.mean(points))
