#For this challenge, create a bank account class that has two attributes:
#owner
#balance

#and two methods:
#deposit
#withdraw

#As an added requirement, withdrawals may not exceed the available balance.
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,deposito):
        self.balance += deposito
        print("Deposit Accepted")

    def withdraw(self,saque):
        if self.balance >= saque:
            self.balance -= saque
            print("Withdraw Accepted")
        else:
            print("Withdraw Unavailable")

acct1 = Account("Jose", 100)
acct1.deposit(1000)
acct1.withdraw(900)
acct1.withdraw(900)