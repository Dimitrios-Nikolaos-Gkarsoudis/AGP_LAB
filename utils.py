import math
import statistics
import random

def distance(A, B):

    x1, y1 = A
    x2, y2 = B

    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def area(a, b, c):
    
    s = (a + b + c)/2
    return math.sqrt(s*(s - a)*(s - b)*(s - c))


def mean(points):
    points_sum = 0
    for point in points:
        points_sum += point

    return points_sum/len(points)   


def median(points):
    sorted_points = sorted(points)
    points_length = len(sorted_points)
    if points_length % 2 == 0:
        return (sorted_points[points_length//2 - 1] + points_length[points_length//2]) / 2
    else:
        return sorted_points[points_length//2] 

def range_of_points(points):
    return max(points) - min(points)

def stdev(points):
    return (sum((x - mean(points))**2 for x in points) / len(points)) ** 0.5

