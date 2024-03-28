import math


def distance(A, B):

    x1, y1 = A
    x2, y2 = B

    return abs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))


def area(a, b, c):

    s = (a + b + c) / 2

    if s * (s - a) * (s - b) * (s - c) > 0:
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        return 0


def mean(list):
    return round(sum(list) / len(list), 2)


def median(list):
    l = len(list)
    list.sort()

    if l % 2 == 0:
        median1 = list[l // 2]
        median2 = list[l // 2 - 1]
        median = (median1 + median2) / 2
        return round(median, 2)
    else:
        median = list[l // 2]
        return round(median, 2)


def range_of_points(list):
    return round(max(list) - min(list), 2)


def stdev(list):
    mean = sum(list) / len(list)
    variance = sum([((x - mean) ** 2) for x in list]) / len(list)
    res = variance**0.5
    return round(res, 2)
