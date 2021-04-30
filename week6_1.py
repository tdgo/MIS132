# MIS 132 - April 30
# Account class

class Account:

    def __init__(self, balance, name, branch="Istanbul"):
        self.balance = balance
        self.owner = name
        self.branch = branch
        #print(f"An account has been created with {self.balance} balance.")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} dollars deposited into the account.")
        print(f"The balance is {self.balance} now.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} dollars have been withdrawn from the account.")
            print(f"The balance is {self.balance} now.")
        else:
            print("Error, insufficient funds.")
            print(f"The balance is {self.balance}")

    def __str__(self):
        return f"The balance of this account is {self.balance} and the account is in {self.branch} branch."


my_account = Account(1000, "MIS132", "Izmir")
print(my_account)

my_account.deposit(100)
print("\n")

my_account.withdraw(1101)


