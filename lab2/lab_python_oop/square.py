from lab_python_oop.rectangle import Rectangle
class Square(Rectangle):
    type = "Квадрат"
    def __init__(self, length, color):
        self.length = length
        super().__init__(self.length, self.length, color)

    def __repr__(self):
        return '{} {} цвета, длина {}, площадь {}.'.format(
            self.type,
            self.rect_color._color,
            self.length,
            self.area())