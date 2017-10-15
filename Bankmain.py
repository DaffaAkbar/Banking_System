from Customerclass import Customer
from Accountclass import Account
import  random
import sys
def mainmenu():
    print("choose one of these options\n"
     "1.Get Customer\t"
     "2.Get number of customer\n"
     "3.Add customer\t"
     "4.Deposit\n"
     "5.Withdraw\t"
     "6.Check Balance\n"
     "7.Set Account\t"
     "8.Get Account\n"
     "9.quit\n")
names =[]
firstname = input("please input the firstname")
lastname = input("please input the lastname")
account = input("please input the account")
customer=Customer(firstname,lastname,account)
namelist=(firstname,lastname)
names.append(namelist)
while True:
    ans = input("do you want to input another Customer?")
    if ans =='y':
        firstname = input("please input the firstname")
        lastname = input("please input the lastname")
        account = input("please input the account")
        names.append(namelist)
    else:
        break
money=random.randint(1000,9000)
balance=int(money)
Balance=Account(balance)
def withd ():
    j = int(input("how much do you want withdraw?"))
    Balance.withdraw(j)
    if Balance.getbalance() < 0:
        print("not enough money")
        Balance.deposit(j)
        withd()
    else:
        print(Balance.getbalance(), "$")
        main()
def main():
    mainmenu()
    j=input("")
    if j=="1":
        print(customer.getname())
        main()
    if j=="2":
        print(len(names))
        main()
    if j=="3":
        firstname = input("please input the firstname")
        lastname = input("please input the lastname")
        account = input("please input the account")
        names.append(customer.setcustomer(firstname, lastname, account))
        main()
    if j=="4":
        j=int(input("how much do you want to deposit?"))
        Balance.deposit(j)
        print(Balance.getbalance(),"$")
        main()
    if j=="5":
        withd()
    if j=="6":
        print(Balance.getbalance(),"$")
        main()
    if j=="7":
        account = input("please input the account")
        customer.setaccount(account)
        main()
    if j=="8":
        print(customer.getaccount())
        main()
    if j=="9":
        sys.exit()
    else:
        print("error")
        main()
main()