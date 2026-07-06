class Account:
    def __init__(self, first_name, last_name, pin, number):
        self.name = first_name + " " + last_name
        self.pin = pin
        self.number = number
        self.balance = 0

    def get_number(self):
        return self.number

    def get_name(self):
        return self.name

    def get_balance(self, pin):
        if self.validate_pin(pin):
            raise ValueError("Invalid Pin")
        return self.balance

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance += deposit_amount
        else:
            raise ValueError("Invalid deposit amount")

    def withdraw(self, amount, pin):
        if self.validate_pin(pin):
            raise ValueError("Invalid Pin")

        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def validate_pin(self, pin):
        return self.pin != pin