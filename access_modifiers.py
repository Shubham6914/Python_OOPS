"""Design a class Employee to manage employee details securely using proper encapsulation and access modifiers. The class should implement the following attributes and methods :

Attributes :

name (string) : public, Represents the name of employee.
employeeId (Integer) : protected, Represents the unique Id of the employee.
salary (double) : private, Represents the salary of the employee.
Methods :

setSalary (double salary) : Sets the salary value, If salary is negative then print "Invalid salary" and set the salary to 0.
getSalary() : Return the salary value.
parameterised constructor to initialize the attributes. (If salary is negative then print "Invalid salary" and set the salary to 0.)
displayEmployeeDetails() : Display the employee details in format specified below :


Refer the sample examples for understanding the output format.

Refer the commented code to check the output statments.


Examples:
Input : name = "Striver" , employeeId = 9656 , salary = 10000 , newSalary = 15840

Output :

Salary : 10000.00

Name : Striver

Employee Id : 9656

Salary : 15840.00"""



class Employee:

    # this is way to define  default and parameterised  constructor in python 
    def __init__(self, name=None, employeeID=None, salary = None, newSalary=None):
        
        self.name = name  #public attribute 
        self._employeeID = employeeID  #protected attribute 
        if salary < 0:
            self.__salary = 0
        
        else:
            self.__salary = salary     #private attribute 
        
        
    # method to set salary with new salary 
    
    def setSalary(self, newSalary):
        if newSalary < 0:
            print(f"Invalid salary:{newSalary}")
            self.__salary = 0
        else:
            self.__salary = newSalary
            
    
    # method to get salar 
    def getSalary(self):
        return self.__salary
    
    
    # method to display Employee Details 
    
    def employeeDetails(self):
        print(f"salary :{self.__salary}", end='\n')
        print(f"Name :{self.name}", end='\n')
        print(f"employeID :{self._employeeID}", end='\n')
        

def main():
    Employee1 = Employee("shubham", 12453, 2500)
    print(f"newSalary :{Employee1.getSalary():.2f}", end='\n')
    Employee1.setSalary(1000)
    # Employee1.getSalary()
    Employee1.employeeDetails()

if __name__ == "__main__":
    main()