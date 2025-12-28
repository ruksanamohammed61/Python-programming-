import math

# Base class
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


# Circle class
class Circle(Shape):
    def get(self):
        self.r = float(input("Enter radius: "))

    def area(self):
        print("Area of Circle:", math.pi * self.r * self.r)

    def perimeter(self):
        print("Perimeter of Circle:", 2 * math.pi * self.r)


# Triangle class
class Triangle(Shape):
    def get(self):
        self.a, self.b, self.c = map(float, input("Enter three sides: ").split())

    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        print("Area of Triangle:", area)

    def perimeter(self):
        print("Perimeter of Triangle:", self.a + self.b + self.c)


# Square class
class Square(Shape):
    def get(self):
        self.s = float(input("Enter side length: "))

    def area(self):
        print("Area of Square:", self.s * self.s)

    def perimeter(self):
        print("Perimeter of Square:", 4 * self.s)


# --- Main program ---
# Circle
c1 = Circle()
c1.get()
c1.area()
c1.perimeter()

# Triangle
t1 = Triangle()
t1.get()
t1.area()
t1.perimeter()

# Square
s1 = Square()
s1.get()
s1.area()
s1.perimeter()
