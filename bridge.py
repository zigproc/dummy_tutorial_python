class DrawingAPIOne(object):
    """ Implementation specific abstraction: concrete class one"""
    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({},{} with radius {})").format(x, y, radius)


class DrawingAPITwo(object):
    """ Implementation specific abstraction: concrete class one"""
    def draw_circle(self, x, y, radius):
       print("API 2 drawing a circle at ({},{} with radius {})").format(x, y, radius)


class Circle(object):
    """ Implementation specific abstraction: """

    def __init__(self, x, y, radius, drawing_api):
        """ Initialize the necessary attributes """
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """ Implmentation specific abstraction taken care by another class """
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        self._radius *= percent


# Build the first circle using API 1
circle1 = Circle(1, 2, 3, DrawingAPIOne())
# draw
circle1.draw()

# Build the first circle using API 1
circle2 = Circle(2, 3, 4, DrawingAPITwo())
# draw
circle2.draw()
