from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
class Rectangle(Figure):
    type = "Прямоугольник"
    def __init__(self, width, high, color):
        self.width = width
        self.high = high
        self.rect_color = Color(color)
    def area(self):
        return self.width * self.high
    def __repr__(self):
       return '{} {} цвета, ширина {}, высота {}, площадь {}.'.format(
            self.type,
            self.rect_color._color,
            self.high,
            self.width,
            self.area())