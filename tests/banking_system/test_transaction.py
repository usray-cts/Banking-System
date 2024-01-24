```python
import pytest
from account import Account
from transaction import Transaction
from unittest.mock import Mock

# Unit tests for the Transaction class
class TestTransaction:

    # Scenario 1: Initialization of `Transaction` Class
    def test_init(self):
        # Creating a new `Transaction` object with a valid `Account` object.
        account = Mock(spec=Account)
        transaction = Transaction(account)
        assert transaction.account == account

        # Creating a new `Transaction` object with an invalid input (not an `Account` object).
        with pytest.raises(TypeError):
            Transaction("Invalid input")

    # Scenario 2: Deposit Method
    def test_deposit(self):
        account = Mock(spec=Account)
        transaction = Transaction(account)

        # Depositing a positive amount.
        account.deposit.return_value = 100
        assert transaction.deposit(100) == "Deposit successful. New balance is 100"

        account.deposit.return_value = 1200
        assert transaction.deposit(200) == "Deposit successful. New balance is 1200"

        # Depositing a negative amount.
        account.deposit.return_value = -100
        assert transaction.deposit(-100) == "Deposit successful. New balance is -100"

        account.deposit.return_value = 800
        assert transaction.deposit(-200) == "Deposit successful. New balance is 800"

        # Depositing zero.
        account.deposit.return_value = 0
        assert transaction.deposit(0) == "Deposit successful. New balance is 0"

        account.deposit.return_value = 1000
        assert transaction.deposit(0) == "Deposit successful. New balance is 1000"

    # Scenario 3: Withdraw Method
    def test_withdraw(self):
        account = Mock(spec=Account)
        transaction = Transaction(account)

        # Withdrawing a positive amount that is less than or equal to the account balance.
        account.withdraw.return_value = 900
        assert transaction.withdraw(100) == "Withdrawal successful. New balance is 900"

        account.withdraw.return_value = 0
        assert transaction.withdraw(1000) == "Withdrawal successful. New balance is 0"

        # Withdrawing a positive amount that is greater than the account balance.
        account.withdraw.return_value = "Insufficient funds"
        assert transaction.withdraw(1100) == "Insufficient funds"

        account.withdraw.return_value = "Insufficient funds"
        assert transaction.withdraw(2000) == "Insufficient funds"

        # Withdrawing a negative amount.
        account.withdraw.return_value = 1100
        assert transaction.withdraw(-100) == "Withdrawal successful. New balance is 1100"

        account.withdraw.return_value = 3000
        assert transaction.withdraw(-2000) == "Withdrawal successful. New balance is 3000"

        # Withdrawing zero.
        account.withdraw.return_value = 1000
        assert transaction.withdraw(0) == "Withdrawal successful. New balance is 1000"

        account.withdraw.return_value = 0
        assert transaction.withdraw(0) == "Withdrawal successful. New balance is 0"

    # Scenario 4: Edge Cases
    def test_edge_cases(self):
        account = Mock(spec=Account)
        transaction = Transaction(account)

        # Handling floating point numbers for deposit and withdrawal amounts.
        account.deposit.return_value = 100.50
        assert transaction.deposit(100.50) == "Deposit successful. New balance is 100.5"

        account.withdraw.return_value = 899.50
        assert transaction.withdraw(100.50) == "Withdrawal successful. New balance is 899.5"

        # Handling very large numbers for deposit and withdrawal amounts.
        account.deposit.return_value = 1e6
        assert transaction.deposit(1e6) == "Deposit successful. New balance is 1000000.0"

        account.withdraw.return_value = 9e6
        assert transaction.withdraw(1e6) == "Withdrawal successful. New balance is 9000000.0"
```
