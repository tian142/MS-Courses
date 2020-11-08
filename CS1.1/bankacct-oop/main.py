import random
import string


class BankAccount:
    def __init__(self, full_name, balance):
        self.full_name = full_name
        self.account_number = ''.join(random.choices(string.digits, k=8))
        self.routing_number = 123456789
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def get_balance(self):
        print(f"Hello! Your account balance is: ${self.balance}")

    def print_receipt(self):
        print(f"{self.full_name}")
        print(f"Account No.:{self.account_number}")
        print(f"Routing No.:{self.routing_number}")
        print(f"Balance: ${self.balance}")


a1 = BankAccount('John Olsson', 12)

a1.print_receipt()
a1.deposit(200)
a1.print_receipt()
a1.withdraw(100)
a1.print_receipt()
a1.add_interest()
a1.get_balance()
