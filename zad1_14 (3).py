import math

class Figure:
    def perimeter(self):
        pass

    def area(self):
        pass


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

class Rectangle(Figure):
    def __init__(self, height, length):
        self.height = height
        self.length = length

    def perimeter(self):
        return 2 * (self.height + self.length)

    def area(self):
        return self.height * self.length

class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        half = self.perimeter() / 2
        return math.sqrt(half * (half - self.side1) * (half - self.side2) * (half - self.side3))

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

class Diamond(Figure):
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def perimeter(self):
        return 4 * math.sqrt((0.5 * self.diagonal1) ** 2 + (0.5 * self.diagonal2) ** 2 )

    def area(self):
        return 0.5 * self.diagonal1 * self.diagonal2

class Trapeze(Figure):
    def __init__(self, side1, side2, height):
        self.side1 = side1
        self.side2 = side2
        self.height = height

    def perimeter(self):
        return self.side1 + self.side2 + 2 * math.sqrt(((self.side2 - self.side1) / 2) ** 2 + self.height ** 2)

    def area(self):
        return 0.5 * (self.side1 + self.side2) * self.height


print("Wybierz figurę:\n 1. Kwadrat\n 2. Prostokąt\n 3. Trójkat\n 4. Koło\n 5. Romb\n 6. Trapez")

choice = int(input("Wybierz figurę:"))

if choice == 1:
    side = float(input("Podaj długość boku kwadratu:"))
    square = Square(side)
    print("Obwód kwadratu:", square.perimeter())
    print("Pole kwadratu:", square.area())

elif choice == 2:
    height = float(input("Podaj wyskość prostokąta:"))
    length = float(input("Podaj długość prostokąta:"))
    rectangle = Rectangle(height, length)
    print("Obwód:", rectangle.perimeter())
    print("Pole:", rectangle.area())

elif choice == 3:
    side1 = float(input("Podaj długośc pierwszego boku:"))
    side2 = float(input("Poadaj długość drugiego boku:"))
    side3 = float(input("Podaj długość trzeciego boku:"))
    triangle = Triangle(side1, side2, side3)
    print("Obwód", triangle.perimeter())
    print("Pole", triangle.area())

elif choice == 4:
    radius = float(input("Podaj promień okręgu:"))
    circle = Circle(radius)
    print("Obwód:", circle.perimeter())
    print("Pole:", circle.area())

elif choice == 5:
    diagonal1 = float(input("Podaj pierwszą przekątną rombu:"))
    diagonal2 = float(input("Podaj drugą przkątną rombu:"))
    diamond = Diamond(diagonal1, diagonal2)
    print("Obwód:", diamond.perimeter())
    print("Pole", diamond.area())

elif choice == 6:
    side1 = float(input("Podaj pierwszą podstawę trapezu:"))
    side2 = float(input("Podaj drugą podstawę trapezu:"))
    height = float(input("Podaj wysokość trapezu:"))
    trapeze = Trapeze(side1, side2, height)
    print("Obwód:", trapeze.perimeter())
    print("Pole:", trapeze.area())

else:
    print("zła wartość\n spróbój jeszcze raz\n Wybierz figurę:\n 1. Kwadrat\n 2. Prostokąt\n 3. Trójkat\n 4. Koło\n 5. Romb\n 6. Trapez")
