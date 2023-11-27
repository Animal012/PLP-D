from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
def main():
    r = Rectangle(13, 13, "синего")
    c = Circle(13, "зеленого")
    s = Square(13, "красного")
    print(r)
    print(c)
    print(s)
if __name__ == "__main__":
    main()