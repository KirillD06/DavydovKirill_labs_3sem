from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    name = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)

    def __repr__(self):
        return "{} {}, сторона {}, площадь {:.2f}".format(
            self.name, self.color.color, self.width, self.area()
        )
