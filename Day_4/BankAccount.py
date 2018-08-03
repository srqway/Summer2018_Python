class BankAccount: #defines our class
    def __init__(self, bal):
        self.__balance = bal

    def deposit(self, amount): #deposit method
        self.__balance += amount #add deposit amount to the balance

    def withdraw(self, amount):# withdraw method
        if self.__balance >= amount: #checking to ensure balance is
                                     #greater than amount to withdraw
            self.__balance -= amount #subtract withdraw amount from the balance
        else:
            print("Error: Insufficient Funds.  Deposit more money")
    def get_balance(self):  #get_balance method      
        return self.__balance
