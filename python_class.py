"""
You are tasked with designing a class Student that stores and displays information about students.

The class must have the following :



Attributes :

name (string) : Stores the name of the student.
rollNumber (int) : Stores the roll number of the student
Methods :

setDetails (String name, int rollNumber) : This method initializes the attributes name and rollNumber with the values provided by the user.
displayDetails() : This method prints the details of the student in following format (The output consist of two separate lines) :


Refer the sample input example to understand the output format.

Refer the commented code on IDE for output statements."""


# student class frepersent business login 
class Student:
    
    # here __init__ is constructor in python 
    def __init__(self,name ,rollNumber):
        self.name = name
        self.rollNumber = rollNumber
        
    
    def setDetails(self, name,rollNumber):
        self.name = name
        self.rollNumber =rollNumber
    
    def displayDetails(self):
        return(self.name, self.rollNumber)
    
    
# Driver Code Starts Here
def main():
    # create an instance of class
    
    student1 = Student("initial name", 0)
    
    # set actual details 
    student1.setDetails("shubham",5678)
    
    # display student info
    name ,rollNumber  = student1.displayDetails()
    
    print("Student Info:")
    print("Student Name:",name)
    print("Student Roll Number:", rollNumber)


# run the driver code 
        
if __name__ == "__main__":
    main()