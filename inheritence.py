"""You are tasked with creating a class hierarchy to represent employees in a company. 
Implement a base class Employee and derive classes Manager and Engineer from it. 
The base class should encapsulate common attributes, and the derived classes should add
specific attributes while overriding methods. The derived classes should explicitly call 
the constructor of the parent class (Employee) to initialize common attributes.

The classes should consist of below specifications :

Base Class: Employee

Attributes : 1) name (string) : Represents the name of the employee.
2) id (Integer) : Unique identifier for the employee.

Methods : 1) displayDetails () : Prints the name and id.


Derived Classes : a) Manager

Attributes : 1) teamSize (Integer) : The size of team managed.
Methods : 1) displayDetails () : calls the parent class method displayDetails() and then prints teamSize.
b) Engineer

Attributes : 1) specialization (string) : The engineer's area of interest.
Methods : 1) displayDetails () : Calls the parent class method displayDetails() and then prints the specialization.


Refer the sample examples for understanding the output format.

The commented code has the output statements return, in order to avoid wrong answers due to case matching or whitespace.



The sample Input follows below naming convention

M -> Prefix of M means input to class Manager

E -> Prefix of E means input to class Engineer


Examples:
Input : M_name = "Jax" , M_id = 101 , M_teamSize = 8

E_name = "William" , E_id = 202 , E_specialization = "Backend Developer"



Output :

Manager Details

Name : Jax

Id : 101

Team Size : 8

"""

# Base Class 
class Employee:
    def __init__(self, name=None, EmpID= None):
        self.name = name
        self.__EmpID = EmpID  #private attribut 
        
        
    def DisplayDetails(self):
        print(f"Name : {self.name}", end='\n')
        print(f"Employee ID  : {self.__EmpID}", end='\n')
        

# CHild Class
# manager class 
class Manager(Employee):
    def __init__(self, name,EmpID,teamSize = None):
        super().__init__(name,EmpID) #call parent class constructor 
        self.teamSize = teamSize
    
    
    def DisplayDetails(self):
        # execute the function of parent class and also known as method overiding 
        super().DisplayDetails()
        print(f"Team Size : {self.teamSize}",end='\n')
        
        
#specialisation class
class Engineer(Employee):
    def __init__(self, name, EmpID, teamSize,specializatoin =None):
        super().__init__(name, EmpID) #call manager class constructor 
        self.specializatoin = specializatoin
        
        
    # method to display the details 
    
    def DisplayDetails(self):
        # this class manager class method and that will call parent class constructor 
        super().DisplayDetails() 
        print(f"Specializatoin : {self.specializatoin}",end='\n')
    

    


# define main function        
def main():
    
    print("Manager info :", end='\n')
    manager = Manager("Raj", 345, 10)
    manager.DisplayDetails()
    
    print(end='\n\n\n')
    
    print("Engineer Info :",end='\n')
    engineer = Engineer("Aman", 4567, "Frontend Developer")
    engineer.DisplayDetails()
    

if __name__ == "__main__":
    main()