import random
import string


class BankAccount:
    def __init__(self, full_name, balance):
        self.full_name = full_name
        # found random id generator below on stack overflow
        self.account_number = ''.join(random.choices(string.digits, k=8))
        self.routing_number = 123456789
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount: .2f}")

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= amount
            self.balance -= 10
            return (print('Insufficient funds. Over draft fee of $10 charged.'))
        else:
            self.balance -= amount
            print(f"Amount Withdrawn :${amount: .2f}")

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def get_balance(self):
        print('-----------Account Balance-----------')
        print(f"Hello! Your account balance is: ${self.balance: .2f}")

    def print_receipt(self):
        print('-----------Account Details-----------')
        print(f"{self.full_name}")
        print(f"Account No.: {self.account_number}")
        print(f"Routing No.: {self.routing_number}")
        print(f"Balance: ${self.balance: .2f}")


acct1 = BankAccount('Marry', 200)
acct1.deposit(100)
acct1.print_receipt()

acct2 = BankAccount('Alex', 200)
acct2.withdraw(150)
acct2.get_balance()

acct3 = BankAccount('Joe', 300)
acct3.deposit(300)
acct3.add_interest()
acct3.print_receipt()
