from account import Account

class Bank:
    def __init__(self, name):
        self.name = name
        self.next_account_number = 1001
        self.accounts = []

    def register_customer(self, first_name, last_name, pin):
        account = Account(
            first_name,
            last_name,
            pin,
            self.next_account_number
        )
        self.accounts.append(account)
        self.next_account_number += 1
        return account

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_number() == account_number:
                return account

        raise ValueError("Account not found")

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        account.deposit(amount)

    def withdraw(self, account_number, amount, pin):
        account = self.find_account(account_number)
        account.withdraw(amount, pin)

    def check_balance(self, account_number, pin):
        account = self.find_account(account_number)
        return account.get_balance(pin)

    def transfer(self, account_one, account_two, amount, pin):
        sender = self.find_account(account_one)
        receiver = self.find_account(account_two)

        sender.withdraw(amount, pin)
        receiver.deposit(amount)

    def remove_account(self, account_number, pin):
        account = self.find_account(account_number)

        if account.validate_pin(pin):
            raise ValueError("Invalid Pin")

        self.accounts.remove(account)