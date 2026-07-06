import unittest
from bank_account.account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.my_account = Account("Aramide", "Ashiwaju", "4321", 1001)

    def test_that_account_has_account_number(self):
        self.assertEqual(1001, self.my_account.get_number())

    def test_that_i_have_an_account_balance_is_zero_if_i_deposit_200_balance_becomes_200(self):
        self.my_account.deposit(200)
        self.assertEqual(200, self.my_account.get_balance("4321"))

    def test_that_i_deposit_a_negative_amount_it_throws_error(self):
        with self.assertRaises(ValueError):
            self.my_account.deposit(-500)

    def test_that_when_i_check_my_balance_with_correct_pin_i_get_my_balance(self):
        self.my_account.deposit(500)
        self.assertEqual(500, self.my_account.get_balance("4321"))

    def test_that_when_i_check_my_balance_with_wrong_pin_it_throws_error(self):
        with self.assertRaises(ValueError):
            self.my_account.get_balance("1234")

    def test_that_i_have_an_account_balance_is_500_if_i_withdraw_300_balance_is_200(self):
        self.my_account.deposit(500)
        self.my_account.withdraw(300, "4321")
        self.assertEqual(200, self.my_account.get_balance("4321"))

    def test_that_when_i_withdraw_with_wrong_pin_it_throws_error(self):
        self.my_account.deposit(600)
        with self.assertRaises(ValueError):
            self.my_account.withdraw(300, "1234")

    def test_that_withdrawal_more_than_the_balance_throws_error(self):
        self.my_account.deposit(600)
        with self.assertRaises(ValueError):
            self.my_account.withdraw(5000, "1234")
