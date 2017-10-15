
class Account ():
    def __init__(self,balance):
        self.balance=int(balance)
    def getbalance(self):
        return self.balance
    def deposit(self,balance):
        self.balance=self.balance+balance
    def withdraw(self,balance):
        self.balance=self.balance-balance

