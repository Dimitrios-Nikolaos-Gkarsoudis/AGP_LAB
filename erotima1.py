import random
import statistics
from itertools import combinations
import utils

points = [(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(100)]
count = 0

areas = []
for triangle_points in combinations(points, 3):
    side1 = utils.distance(triangle_points[0], triangle_points[1])
    side2 = utils.distance(triangle_points[1], triangle_points[2])
    side3 = utils.distance(triangle_points[2], triangle_points[0])
    
   
    triangle_area = utils.area(side1, side2, side3)
    areas.append(triangle_area)
    count = count + 1

print("\n")
print("Correct Triangles: ", count)
print("\n")
print("Using utils functions: ")
print("Mean area: ", utils.mean(areas))
print("Median area: ", utils.median(areas))
print("Range: ", utils.range_of_points(areas))
print("Standard deviation of areas: ", utils.stdev(areas))
print("\n")
print("Using statistics functions: ")
print("Mean area: ", round(statistics.mean(areas), 2))
print("Median area: ", round(statistics.median(areas), 2))
print("Standard deviation of areas: ", round(statistics.stdev(areas), 2))





