"""Practice (Constructors)
100
Design a class Rectangle with the following specifications :

Attributes :

length (double) : Represents the length of the rectangle
width (double) : Represents the width of the rectangle.
Area (double) : Represents the area of rectangle.
Constructors :

A default constructor that initializes both length and width to 1.0
A parameterized constructor that takes two arguments to initialize length and width.
Methods :

double calculateArea() : Computes and returns the area of rectngle.
void displayDetails() : Prints the rectangle's details, including its dimensions and area, in format specified below :


Refer the sample examples for understanding the output format.

Refer the commented code on IDE for output statements.


Examples:
Input : length = 5.0 , width = 3.0

Output :

Length : 1.00

Width : 1.00

Area : 1.00

Length : 5.00

Width : 3.00

Area : 15.00

Explanation :

The program initialize the object r1 of class Rectangle using default constructor.
Then it calls the calculateArea() method using r1 object.
Then it calls the displayDetails() method using r1 object.
Now program initializes another object r2 of class Rectangle using parameterized constructor with length and width as parameters.
Then it calls the calculateArea() method using r2 object.
Then it calls the displayDetails() method using r2 object."""




class Rectangle:

    
    # In python this is how we can handle both default and parameterised constructor
    def __init__(self, length=1.0, width=1.0):
        self.length = length
        self.width = width
        
    
    def calculateArea(self):
        return  self.length * self.width
    
    def displayDetails(self):
        print("Output:\n")
        print(f"Length : {self.length}\n")
        print(f"Width  : {self.width}\n" )
        print(f"Area   : {self.length * self.width}")
        

def main():
    r1 = Rectangle()
    
    # Area of r1 object
    r1.calculateArea()
    r1.displayDetails()
    
    r2 = Rectangle(5.0, 3.0)
    
    # Area of object r2
    r2.calculateArea()
    r2.displayDetails()
    

if __name__ ==  "__main__":
    main()