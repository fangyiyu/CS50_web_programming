class Point:
    # A method defining how to create a point: (self shoule be the first argument for any method within a Python class)
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 5)
print(p.x)
print(p.y)
