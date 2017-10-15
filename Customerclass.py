from Accountclass import Account
class Customer():
    def __init__(self,firstname,lastname,account):
        self.__firstname=firstname
        self.__lastname=lastname
        self.__account=account
    def getfirst(self):
        return self.__firstname
    def getlast(self):
        return self.__lastname
    def getaccount(self):
        return self.__account
    def setaccount(self,account):
        self.__account=account
    def setcustomer(self,firstname,lastname,account):
        customer = Customer(firstname,lastname,account)
        return customer
    def getname(self):
        print("Customer:",self.__firstname,self.__lastname)
