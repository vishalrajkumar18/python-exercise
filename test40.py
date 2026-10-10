import math
# imports the math module for square root calculation
p1 = [4, 0]
# coordinates of the first point (x1, y1)
p2 = [6, 6]
# coordinates of the second point (x2, y2)
distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
# calculates distance between two points using Euclidean formula
print("Distance:", distance)
# displays the calculated distance
