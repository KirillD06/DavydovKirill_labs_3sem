import math
from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor

class Circle(Figure):
    name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return math.pi * self.radius * self.radius

    def __repr__(self):
        return "{} {}, радиус {}, площадь {:.2f}".format(
            self.name, self.color.color, self.radius, self.area()
        )
