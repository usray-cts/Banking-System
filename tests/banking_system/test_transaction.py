```python
import pytest
from unittest.mock import Mock
from account import Account
from transaction import Transaction

# Create a fixture for the account
@pytest.fixture
def account():
    account = Account()
    account.deposit = Mock()
    account.withdraw = Mock()
    return account

# Create a fixture for the transaction
@pytest.fixture
def transaction(account):
    return Transaction(account)

def test_deposit_positive(transaction):
    transaction.account.deposit.return_value = 100
    assert transaction.deposit(100) == "Deposit successful. New balance is 100"

def test_deposit_zero(transaction):
    transaction.account.deposit.return_value = 0
    assert transaction.deposit(0) == "Deposit successful. New balance is 0"

def test_deposit_negative(transaction):
    transaction.account.deposit.return_value = "Invalid amount"
    assert transaction.deposit(-100) == "Invalid amount"

def test_withdraw_less_than_balance(transaction):
    transaction.account.withdraw.return_value = 50
    assert transaction.withdraw(50) == "Withdrawal successful. New balance is 50"

def test_withdraw_equal_to_balance(transaction):
    transaction.account.withdraw.return_value = 0
    assert transaction.withdraw(100) == "Withdrawal successful. New balance is 0"

def test_withdraw_more_than_balance(transaction):
    transaction.account.withdraw.return_value = "Insufficient balance"
    assert transaction.withdraw(200) == "Insufficient balance"

def test_withdraw_zero(transaction):
    transaction.account.withdraw.return_value = 100
    assert transaction.withdraw(0) == "Withdrawal successful. New balance is 100"

def test_withdraw_negative(transaction):
    transaction.account.withdraw.return_value = "Invalid amount"
    assert transaction.withdraw(-50) == "Invalid amount"

def test_deposit_withdraw(transaction):
    transaction.account.deposit.return_value = 100
    transaction.account.withdraw.return_value = 50
    assert transaction.deposit(100) == "Deposit successful. New balance is 100"
    assert transaction.withdraw(50) == "Withdrawal successful. New balance is 50"

def test_deposit_withdraw_same_amount(transaction):
    transaction.account.deposit.return_value = 100
    transaction.account.withdraw.return_value = 0
    assert transaction.deposit(100) == "Deposit successful. New balance is 100"
    assert transaction.withdraw(100) == "Withdrawal successful. New balance is 0"

def test_deposit_withdraw_more_than_amount(transaction):
    transaction.account.deposit.return_value = 100
    transaction.account.withdraw.return_value = "Insufficient balance"
    assert transaction.deposit(100) == "Deposit successful. New balance is 100"
    assert transaction.withdraw(200) == "Insufficient balance"

def test_deposit_withdraw_large_amount(transaction):
    transaction.account.deposit.return_value = 1e18
    transaction.account.withdraw.return_value = 0
    assert transaction.deposit(1e18) == "Deposit successful. New balance is 1000000000000000000"
    assert transaction.withdraw(1e18) == "Withdrawal successful. New balance is 0"
```
