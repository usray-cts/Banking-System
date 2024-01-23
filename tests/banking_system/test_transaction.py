```python
import pytest
from unittest.mock import Mock, MagicMock
from account import Account
from transaction import Transaction

# Define a fixture for the account object
@pytest.fixture
def account():
    account = Account()
    account.deposit = MagicMock()
    account.withdraw = MagicMock()
    return account

# Define a fixture for the transaction object
@pytest.fixture
def transaction(account):
    return Transaction(account)

# Scenario 1: Deposit operation with valid amount
def test_deposit_valid_amount(transaction, account):
    account.deposit.return_value = 6000
    assert transaction.deposit(1000) == "Deposit successful. New balance is 6000"

# Scenario 2: Deposit operation with invalid amount
def test_deposit_invalid_amount(transaction):
    with pytest.raises(TypeError):
        transaction.deposit("one thousand")

# Scenario 3: Withdraw operation with valid amount
def test_withdraw_valid_amount(transaction, account):
    account.withdraw.return_value = 4000
    assert transaction.withdraw(1000) == "Withdrawal successful. New balance is 4000"

# Scenario 4: Withdraw operation with invalid amount
def test_withdraw_invalid_amount(transaction):
    with pytest.raises(TypeError):
        transaction.withdraw("one thousand")

# Scenario 5: Multiple deposit and withdrawal operations
def test_multiple_operations(transaction, account):
    account.deposit.return_value = 6000
    assert transaction.deposit(1000) == "Deposit successful. New balance is 6000"
    account.withdraw.return_value = 5500
    assert transaction.withdraw(500) == "Withdrawal successful. New balance is 5500"
    account.deposit.return_value = 7500
    assert transaction.deposit(2000) == "Deposit successful. New balance is 7500"
    account.withdraw.return_value = 6000
    assert transaction.withdraw(1500) == "Withdrawal successful. New balance is 6000"

# Scenario 6: Edge cases
def test_edge_cases(transaction):
    with pytest.raises(ValueError):
        transaction.deposit(1000.999)
    with pytest.raises(ValueError):
        transaction.withdraw(1000.999)
    with pytest.raises(ValueError):
        transaction.deposit(1e100)
    with pytest.raises(ValueError):
        transaction.withdraw(1e100)
```
