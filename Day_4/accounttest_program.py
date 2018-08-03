import BankAccount

def main():
    #balance = 1500 hardcode the amount
    #savings_acct = BankAccount.BankAccount(1500)
    
    balance = float(input('Enter starting balance: ')) #allows user to enter the amount

    savings_acct = BankAccount.BankAccount(balance) # created an instance of class BankAccount

    print('Available starting balance is: $',format(savings_acct.get_balance(), ',.2f'))

    deposit_amount = float(input('Enter amount of deposit: '))

    print('Depositing $', format(deposit_amount,',.2f')) #prints amount to deposit
    
    savings_acct.deposit(deposit_amount) #deposit money using deposit method
    
    print('Current balance is: $',format(savings_acct.get_balance(), ',.2f'))

    withdraw_amount = float(input('Enter the amount to withdraw: '))

    print('Withdrawing $', format(withdraw_amount,',.2f'))

    savings_acct.withdraw(withdraw_amount) #withdraw money using withdraw method
    
    print('Current balance is: $',format(savings_acct.get_balance(), ',.2f'))
        
main()

