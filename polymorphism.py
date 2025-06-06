"""Practice (Polymorphism)

Design a class ShapeCalculator that calculates the area of different shapes using method overloading. Implement the below attributes and methods to calculate the area of different shapes :

Methods :

area (integer radius) : Calculates and print the area of circle using the formula π×radius2 .
area (integer length, integer width) : Calculates and print the area of rectangle using the formula (length * width).
area (integer base1, integer base2, integer height) : Calculates and print the area of Trapezoid using the formula ( (base1 + base2) * height) / 2.


Refer the sample examples for understanding the output format.

Refer the commented code for the output statements.

Consider π = 3.14


Examples:
Input : radius = 2 , length = 2 , width = 3 , base1 = 2 , base2 = 3, height = 2

Output :

Area of Circle : 12

Area of Rectangle : 6

Area of Trapezoid : 5

Explanation :

We create the object of the class ShapeCalculator.
Calls the area method with radius as argument. It calculates and prints the area of circle.
Calls the area method with length and width as arguments. It calculates and prints the area of rectangle.
Calls the area method with base1, base2, height as arguments. It calculates and prints the area of trapezoid.



"""

class ShapeCalculator:
    def area(self, *args):
        pi = 3.14

        if len(args) == 1:
            radius = args[0]
            circle_area = int(pi * (radius ** 2))
            print(f"Area of Circle : {circle_area}")

        elif len(args) == 2:
            length, width = args
            rectangle_area = int(length * width)
            print(f"Area of Rectangle : {rectangle_area}")

        elif len(args) == 3:
            base1, base2, height = args
            trapezoid_area = int(((base1 + base2) * height) / 2)
            print(f"Area of Trapezoid : {trapezoid_area}")

        else:
            print("Invalid number of arguments")

       

def main():
    calculate = ShapeCalculator()
    calculate.area(2)
    calculate.area(2, 3)
    calculate.area(2,3,2)
    calculate.area(3,4,5,6,8)
    

if __name__ == "__main__":
    main()