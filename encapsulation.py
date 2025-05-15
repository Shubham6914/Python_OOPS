"""
You are tasked to design a class Book to manage the book details in a library. The class should contain the following specifications :

Attributes :

title (array<string>) : The title of the book (public).
author (array<string>) : The author of the book (public)
isAvailable (array<boolean>) : The availability status of the book (private).
Methods :
    Parameterised constructor to initialize the title, author, isAvaialble list.
    
    
borrowBook(string bookName) : If the availability status for book 'bookName' is true then the book can be borrowed,
    Once borrowed mark its status as false. If availability status for book 'bookname' is false then the book is already
    borrowed by some user and cannot be borrowed until its returned, so return "Book Not Available".
    
returnBook (string bookName) : The book with bookName is returned and should be marked as available by 
        setting its available flag to true.
        
getAvailability (string bookName) : Prints the availability status of the book with name 'bookName' 
        (true for available , false for unavailable).


Refer the sample example to understand the output format.

Refer the commented code on IDE to view the output statements.



The Input is provided as mentioned below :

"1 <book name>" - represents call to borrowBook method along with name of the book to borrow.

"2 <book name>" - represents call to returnBook method along with name of the book to return.

"3 <book name>" - represents call to getAvailability method along with name of book.


"""
from typing import List
class BookLibrary:
    
    # initialise parameterised constructor with public and private variables 
    def __init__(self, title:List,author:List,isAvaialble:List):
        self.title = title                #public variable
        self.author = author              #public variable
        self.__isAvaialble = isAvaialble  #private variable
        
    # method for borrowBook
    def borrowBook(self, bookName):
        found = False
        for i in range(len(self.title)):
            if bookName ==  self.title[i]:
                found = True
                if self.__isAvaialble[i] == True:
                    print("Book is Available")
                    self.__isAvaialble[i] = False
                else:
                    print("Book Not Available")
        if not found:
            print(f"{bookName} Not Found")  

            
    # method for returning book which is available 
    
    def returnBook(self, bookName):
        found = False
        for i in range(len(self.title)):
            if bookName == self.title[i]: 
                found = True
                self.__isAvaialble[i] = True
                return self.bookName, self
        if not found:
            print(f"There is no book with this {bookName}")  
            
    #  method for printing the status of books availability 
    
    def getAvailability(self, bookName):
        found = False
        for i in range(len(self.title)):
            if bookName == self.title[i]:
                found = True
                print(f"Book of Status: {self.__isAvaialble[i]}")
        if not found:
            print(f"{bookName} Status Not Found")
  

                
        
        

def main():
    title = [ "Sherlock_Holmes", "Frankenstein", "King_Arthur_and_the_Round_Table", "Treasure_Island" ]

    author = [ "Arthur_Conan_Doyle", "Mary_Shelley", "Roger_Lancelyn_Green", "Robert_Louis_Stevenson" ]

    isAvailable = [ False, True, False, False ]

                
        
        
    book = BookLibrary(title,author,isAvailable)
    book.borrowBook("Frankenstein")
    book.returnBook("Frankenstein")
    book.getAvailability("Frankenstein")
    

if __name__ == "__main__":
    main()
        
    
    