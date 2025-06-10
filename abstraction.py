"""Practice (Abstraction)
100
You are required to design a program that utilizes an abstract class Animal to serve as the foundation for specific animal classes. The objective is to demonstrate runtime polymorphism where derived classes override the behaviour of the abstract method makeSound(). The program should include:

An abstract class Animal :

Attributes :

name (string) : Represents the name of the animal.
Abstract Method :

makeSound() : To print the sound specific to the animal.
Derived Classes :

Dog class : Inherits class Animal and overrides the makeSound() method to print "Woof!".
Cat class : Inherits class Animal and overrides the makeSound() method to print "Meow!".


Refer sample example to understand about the output format.

Refer the commented code on IDE to view the output statements.


Examples:
Input : d_name = "Buddy" , c_name = 'Whiskers"

Output :

The dog Buddy says : Woof!

The cat Whiskers says : Meow!

Explanation :

First the object of Dog class is created with the name provided for the dog.
Then the dog object is used to call the makeSound() method to print the output for the dog.
Now the object of Cat class is created with name provided for the cat.
Then the cat object is used to call the makeSound() method to print the output for the cat."""


from abc import ABC, abstractmethod


class Animal(ABC):
    # created constructor to take attribute name 
    def __init__(self, name=None):
        self.name = name
        
    # initialise method makesound to produce animals sound 
    @abstractmethod
    def makeSound(self, sound=None):
        pass

# dog class inherit parent class Animal 
class Dog(Animal):
    def makeSound(self, sound=None):
        print(f"The dog {self.name} says : {sound}\n")
        

# cat class inherit parent class Animal 

class Cat(Animal):
    def makeSound(self, sound=None):
        print(f"The cat {self.name} says : {sound}")
        
        

def main():
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    dog.makeSound("Woof!")
    cat.makeSound("Meow!")

if __name__ == "__main__":
    main()