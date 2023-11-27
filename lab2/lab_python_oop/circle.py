from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
import math
class Circle(Figure):
    type = "Круг"
    def __init__(self, radius, color):
        self.radius = radius
        self.circle_color = Color(color)
    def area(self):
       return math.pi * (self.radius ** 2)

    def __repr__(self):
        return '{} {} цвета, радиус {}, площадь {}.'.format(
            self.type,
            self.circle_color._color,
            self.radius,
            self.area())