class Bank:
    def __init__(self,acc_no,name,acc_type,balance):
        self.acc_no=acc_no
        self.name=name
        self.acc_type=acc_type
        self.balance=balance

    def deposit(self,amnt):
        self.balance+=amnt
        print("Deposited: ",amnt)

    def withdraw(self,amnt):
        if amnt>self.balance:
            print("Not enough balance!!!")
        else:
            self.balance-=amnt
            print("Withdrawn: ",amnt)

acc_no=int(input("Enter account number: "))
name=input("Enter name: ")
acc_type=input("Enter account type: ")
balance=float(input("Enter starting balance: "))

acc=Bank(acc_no,name,acc_type,balance)

amnt=float(input("\nEnter amount to deposit: "))
acc.deposit(amnt)

amnt=float(input("\nEnter amount to withdraw: "))
acc.withdraw(amnt)

print("\nFinal balance: ",acc.balance)
