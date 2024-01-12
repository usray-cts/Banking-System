```python
import pytest
from account import Account

# Unit test code

# Scenario 1: Account Initialization
def test_account_initialization():
    account = Account(123456)
    assert account.account_number == 123456
    assert account.balance == 0

    account = Account(123456, 100)
    assert account.account_number == 123456
    assert account.balance == 100

# Scenario 2: Deposit Functionality
def test_deposit():
    account = Account(123456)
    assert account.deposit(100) == 100
    assert account.deposit(0) == 100
    with pytest.raises(ValueError):
        account.deposit(-100)

# Scenario 3: Withdraw Functionality
def test_withdraw():
    account = Account(123456, 100)
    assert account.withdraw(50) == 50
    assert account.withdraw(50) == 0
    assert account.withdraw(50) == "Insufficient balance"
    with pytest.raises(ValueError):
        account.withdraw(-50)

# Scenario 4: Multiple Deposits and Withdrawals
def test_multiple_operations():
    account = Account(123456)
    assert account.deposit(100) == 100
    assert account.deposit(100) == 200
    assert account.withdraw(50) == 150
    assert account.withdraw(50) == 100

# Scenario 5: Edge Cases
def test_edge_cases():
    account = Account(123456)
    assert account.deposit(1e10) == 1e10
    assert account.deposit(0.001) == 1e10 + 0.001
    with pytest.raises(ValueError):
        account.deposit("100")
    with pytest.raises(ValueError):
        account.withdraw("50")
```
