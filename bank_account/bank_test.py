import unittest
from bank_account.bank import Bank

class TestBank(unittest.TestCase):

    def setUp(self):
        self.my_bank = Bank("Access Bank")

    def test_register_account_assigns_name_to_customer(self):
        account = self.my_bank.register_customer("Aramide", "Ashiwaju", "4321")
        self.assertEqual("Aramide Ashiwaju", account.get_name())
        self.assertEqual(1001, account.get_number())

    def test_register_account_assigns_number_to_customer(self):
        self.my_bank.register_customer("Aramide", "Ashiwaju", "4321")
        account = self.my_bank.register_customer("Tobi", "Lander", "1234")
        self.assertEqual(1002, account.get_number())

    def test_find_account_with_account_number_returns_correct_account(self):
        registered = self.my_bank.register_customer("Mide", "Charles", "1914")
        found = self.my_bank.find_account(registered.get_number())
        self.assertEqual(registered, found)

    def test_find_account_with_unknown_number_throws_error(self):
        with self.assertRaises(ValueError):
            self.my_bank.find_account(2222)

    def test_deposit_to_account_account_balance_increases(self):
        account = self.my_bank.register_customer("Mide", "Charles", "1914")
        self.my_bank.deposit(account.get_number(), 1000)
        self.assertEqual(1000, account.get_balance("1914"))

    def test_deposit_to_unknown_account_throws_error(self):
        with self.assertRaises(ValueError):
            self.my_bank.deposit(2222, 2000)

    def test_withdraw_an_amount_balance_decreases(self):
        account = self.my_bank.register_customer("Mide", "Charles", "1914")
        self.my_bank.deposit(account.get_number(), 2000)
        self.my_bank.withdraw(account.get_number(), 1000, "1914")
        self.assertEqual(1000, account.get_balance("1914"))

    def test_withdraw_an_amount_with_wrong_pin_throws_error(self):
        account = self.my_bank.register_customer("Mide", "Charles", "1914")
        self.my_bank.deposit(account.get_number(), 2000)

        with self.assertRaises(ValueError):
            self.my_bank.withdraw(account.get_number(), 1000, "1922")

    def test_withdraw_an_amount_from_unknown_account_throws_error(self):
        with self.assertRaises(ValueError):
            self.my_bank.withdraw(2222, 2000, "1914")

    def test_check_balance_with_account_number_and_password(self):
        account = self.my_bank.register_customer("Mide", "Charles", "1914")
        self.my_bank.deposit(account.get_number(), 2000)
        self.assertEqual(
            2000,
            self.my_bank.check_balance(account.get_number(), "1914")
        )

    def test_check_balance_with_wrong_pin_throws_error(self):
        account = self.my_bank.register_customer("Mide", "Charles", "1914")
        self.my_bank.deposit(account.get_number(), 2000)

        with self.assertRaises(ValueError):
            self.my_bank.check_balance(account.get_number(), "2222")

    def test_check_balance_of_an_unknown_account_throws_error(self):
        with self.assertRaises(ValueError):
            self.my_bank.check_balance(2222, "1914")

    def test_transfer_amount_from_one_account_to_another_account(self):
        sender = self.my_bank.register_customer("Mide", "Charles", "1914")
        receiver = self.my_bank.register_customer("Tolu", "Babs", "4321")

        self.my_bank.deposit(sender.get_number(), 5000)
        self.my_bank.transfer(
            sender.get_number(),
            receiver.get_number(),
            3000,
            "1914"
        )

        self.assertEqual(
            2000,
            self.my_bank.check_balance(sender.get_number(), "1914")
        )
        self.assertEqual(
            3000,
            self.my_bank.check_balance(receiver.get_number(), "4321")
        )

    def test_transfer_with_wrong_pin_throws_error_and_leaves_balance_unchanged(self):
        sender = self.my_bank.register_customer("Mide", "Charles", "1914")
        receiver = self.my_bank.register_customer("Tolu", "Babs", "4321")

        self.my_bank.deposit(sender.get_number(), 5000)

        with self.assertRaises(ValueError):
            self.my_bank.transfer(
                sender.get_number(),
                receiver.get_number(),
                3000,
                "2222"
            )

        self.assertEqual(5000, sender.get_balance("1914"))
        self.assertEqual(0, receiver.get_balance("4321"))

    def test_transfer_more_than_balance_throws_error(self):
        sender = self.my_bank.register_customer("Mide", "Charles", "1914")
        receiver = self.my_bank.register_customer("Tolu", "Babs", "4321")

        self.my_bank.deposit(sender.get_number(), 1000)

        with self.assertRaises(ValueError):
            self.my_bank.transfer(
                sender.get_number(),
                receiver.get_number(),
                3000,
                "1914"
            )

        self.assertEqual(1000, sender.get_balance("1914"))
        self.assertEqual(0, receiver.get_balance("4321"))

    def test_transfer_from_non_existing_account(self):
        receiver = self.my_bank.register_customer("Mide", "Charles", "1914")

        with self.assertRaises(ValueError):
            self.my_bank.transfer(2222, receiver.get_number(), 3000, "4321")

        self.assertEqual(0, receiver.get_balance("1914"))

    def test_transfer_to_non_existing_account(self):
        sender = self.my_bank.register_customer("Mide", "Charles", "1914")
        self.my_bank.deposit(sender.get_number(), 5000)
        with self.assertRaises(ValueError):
            self.my_bank.transfer(sender.get_number(), 2222, 1000, "1914")

        self.assertEqual(5000, sender.get_balance("1914"))

    def test_remove_account_removes_the_account(self):
        self.my_bank.register_customer("Mide", "Charles", "1914")
        account = self.my_bank.register_customer("Tolu", "Babs", "4321")
        self.my_bank.register_customer("Seun", "Jacob", "1234")

        self.my_bank.remove_account(account.get_number(), "4321")

        with self.assertRaises(ValueError):
            self.my_bank.find_account(account.get_number())

    def test_remove_account_with_wrong_pin(self):
        account = self.my_bank.register_customer("Tolu", "Babs", "4321")

        with self.assertRaises(ValueError):
            self.my_bank.remove_account(account.get_number(), "2222")

        self.assertEqual(
            account,
            self.my_bank.find_account(account.get_number())
        )

    def test_remove_non_existing_account_throws_exception(self):
        with self.assertRaises(ValueError):
            self.my_bank.remove_account(4444, "2222")
