```python
import pytest
from account import Account
from transaction import Transaction
from unittest.mock import MagicMock

# Test cases for deposit method
def test_deposit_positive_amount():
    account = Account()
    account.deposit = MagicMock(return_value=600)
    transaction = Transaction(account)
    assert transaction.deposit(100) == "Deposit successful. New balance is 600"

def test_deposit_zero_balance():
    account = Account()
    account.deposit = MagicMock(return_value=100)
    transaction = Transaction(account)
    assert transaction.deposit(100) == "Deposit successful. New balance is 100"

def test_deposit_negative_amount():
    account = Account()
    account.deposit = MagicMock(side_effect=ValueError("Invalid amount"))
    transaction = Transaction(account)
    with pytest.raises(ValueError):
        transaction.deposit(-100)

def test_deposit_non_numeric_value():
    account = Account()
    account.deposit = MagicMock(side_effect=ValueError("Invalid amount"))
    transaction = Transaction(account)
    with pytest.raises(ValueError):
        transaction.deposit("one hundred")

# Test cases for withdraw method
def test_withdraw_less_than_balance():
    account = Account()
    account.withdraw = MagicMock(return_value=400)
    transaction = Transaction(account)
    assert transaction.withdraw(100) == "Withdrawal successful. New balance is 400"

def test_withdraw_equal_to_balance():
    account = Account()
    account.withdraw = MagicMock(return_value=0)
    transaction = Transaction(account)
    assert transaction.withdraw(500) == "Withdrawal successful. New balance is 0"

def test_withdraw_more_than_balance():
    account = Account()
    account.withdraw = MagicMock(return_value="Insufficient funds")
    transaction = Transaction(account)
    assert transaction.withdraw(600) == "Insufficient funds"

def test_withdraw_negative_amount():
    account = Account()
    account.withdraw = MagicMock(side_effect=ValueError("Invalid amount"))
    transaction = Transaction(account)
    with pytest.raises(ValueError):
        transaction.withdraw(-100)

def test_withdraw_non_numeric_value():
    account = Account()
    account.withdraw = MagicMock(side_effect=ValueError("Invalid amount"))
    transaction = Transaction(account)
    with pytest.raises(ValueError):
        transaction.withdraw("one hundred")

# Edge cases
def test_deposit_large_amount():
    account = Account()
    account.deposit = MagicMock(return_value=1000000100)
    transaction = Transaction(account)
    assert transaction.deposit(1000000000) == "Deposit successful. New balance is 1000000100"

def test_withdraw_large_amount():
    account = Account()
    account.withdraw = MagicMock(return_value="Insufficient funds")
    transaction = Transaction(account)
    assert transaction.withdraw(1000000000) == "Insufficient funds"

def test_deposit_small_amount():
    account = Account()
    account.deposit = MagicMock(return_value=0.0000001)
    transaction = Transaction(account)
    assert transaction.deposit(0.0000001) == "Deposit successful. New balance is 0.0000001"

def test_withdraw_small_amount():
    account = Account()
    account.withdraw = MagicMock(return_value=0)
    transaction = Transaction(account)
    assert transaction.withdraw(0.0000001) == "Withdrawal successful. New balance is 0"

def test_deposit_zero():
    account = Account()
    account.deposit = MagicMock(return_value=0)
    transaction = Transaction(account)
    assert transaction.deposit(0) == "Deposit successful. New balance is 0"

def test_withdraw_zero():
    account = Account()
    account.withdraw = MagicMock(return_value=0)
    transaction = Transaction(account)
    assert transaction.withdraw(0) == "Withdrawal successful. New balance is 0"
```
