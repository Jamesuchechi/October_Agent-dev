""" Encapsulation is a fundamental concept in object-oriented programming (OOP) 
that refers to the bundling of data (attributes) and methods (functions)
 that operate on that data into a single unit,typically a class.
It restricts direct access to some of an object's components, which can prevent 
the accidental modification of data and promote a clear interface for interacting with the object."""

class BankAccount:
    def __init__(self, owner, starting_balance):
        self.owner = owner
        self.__balance = starting_balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Nice try, you can't deposit negative money!")

    def get_balance(self):
        return self.__balance

my_account = BankAccount("Alex", 500)
my_account.deposit(100)     
#print(my_account.__balance)  
print(my_account.get_balance()) 