"""Design a class BankAccount with the following specification :

Attributes :

accountNumber (string) : Represents the account number of the user's account
balance (double) : Represents the balance of the account
Constructor :

Implement a parameterised constructor to have the accountNmber and balance initialised while creating the object.
Methods :

deposit (double amount) : It adds the amount to the balance of the user's account.
withdraw (double amount) : It deduct the money (amount) from the balance. If the balance is insufficient then print "Insufficient funds!" and do not change the original amount.
displayDetails() : It diplays th accuntNumber and balance of the account.


Refer the sample examples for understanding the output format.


"""


class BankAccount:
    
    def __init__(self,accountNumber,balance):
        self.__accountNumber =accountNumber
        self.__balance = balance #private attributes in python 
        
        # parameterised constructor
    def setAccountAndBalance(self,accountNumber,balance):
        self.__accountNumber = accountNumber
        self.__balance = balance
    
    # three methods which we have to implement in this deposit,withdraw,displayDetails()
    
    # deposit (double amount) : It adds the amount to the balance of the user's account.
    
    def deposit(self,  ammount):
        try:
            self.__balance += ammount
        except Exception as e:
            print("Account number not provided ")
        
    # withdraw (double amount) : It deduct the money (amount) from the balance. If the balance is insufficient then print "Insufficient funds!" and do not change the original amount.
    
    def withdraw(self,ammount):
        try:
            if self.__balance > ammount:
                self.__balance -= ammount
                
            else:
                print(f"your current {self.__balance} is low")
        except Exception as e   :
            print("Account number not provided ")
    
    def displayDetails(self):
        return self.__accountNumber , self.__balance
    
    
    
def main():
    # "45678912345",5000
    acn = "45678912345"
    current_balance =5000
    deposit_amount = 500
    withdraw_amount = 1000
    
    cusomter = BankAccount("45678912345",200)

    cusomter.setAccountAndBalance(acn,current_balance)
    cusomter.deposit(deposit_amount)
    accountNumber, balance = cusomter.displayDetails()
    print(f"Your Account Number: {accountNumber}\n")
    print(f"{deposit_amount} is credited to your account.")
    print(f"Balance after deposit: {balance}\n")

    cusomter.withdraw(withdraw_amount)
    accountNumber, balance = cusomter.displayDetails()
    print(f"Your Account Number: {accountNumber}\n")
    print(f"{withdraw_amount} is debited from your account.")
    print(f"Balance after withdrawal: {balance}\n")


        
    
if __name__ =="__main__":
    main()  
    
    
    