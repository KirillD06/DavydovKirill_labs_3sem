from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor

class Rectangle(Figure):
    name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "{} {}, ширина {}, высота {}, площадь {:.2f}".format(
            self.name, self.color.color, self.width, self.height, self.area()
        )
