import unittest
from utils import distance, area, mean, median, stdev
from itertools import combinations 

points = []
    
with open ("points.txt", "r") as f:
    for line in f:
        x,y = line.split()
        points.append((int(x), int(y)))
    
areas = []    

class TestPoints(unittest.TestCase):
    def setUp(self):
        self.points = points

    def test_statistic_tests(self):
        count = 0
        areas = []
        for triangle_points in combinations(self.points, 3):
            side1 = distance(triangle_points[0], triangle_points[1])
            side2 = distance(triangle_points[1], triangle_points[2])
            side3 = distance(triangle_points[2], triangle_points[0])
            triangle_area = area(side1, side2, side3)
            areas.append(triangle_area)
            count = count + 1
        self.assertEqual(count, 161671)
        self.assertAlmostEqual(mean(areas), 3206.86, places = 2)
        self.assertAlmostEqual(median(areas), 2392.50, places = 2)
        self.assertAlmostEqual(stdev(areas), 2843.23, places = 2)

if __name__ == '__main__':
    unittest.main()       
