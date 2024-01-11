```python
import pytest
from account import Account

# Test the initialization of the Account class
def test_account_initialization():
    acc = Account('123456', 1000)
    assert acc.account_number == '123456'
    assert acc.balance == 1000

    acc = Account('123456')
    assert acc.account_number == '123456'
    assert acc.balance == 0

    with pytest.raises(Exception):
        acc = Account('123456', -1000)

# Test the deposit method of the Account class
def test_account_deposit():
    acc = Account('123456', 1000)
    acc.deposit(500)
    assert acc.balance == 1500

    acc.deposit(0)
    assert acc.balance == 1500

    with pytest.raises(Exception):
        acc.deposit(-500)

# Test the withdraw method of the Account class
def test_account_withdraw():
    acc = Account('123456', 1000)
    acc.withdraw(500)
    assert acc.balance == 500

    acc.withdraw(500)
    assert acc.balance == 0

    with pytest.raises(Exception):
        acc.withdraw(1500)

    with pytest.raises(Exception):
        acc.withdraw(-500)

# Test the Account class with non-numeric account number
def test_account_non_numeric():
    with pytest.raises(Exception):
        acc = Account('abc123')
        acc = Account(True)

# Test the deposit method of the Account class with non-numeric amount
def test_account_deposit_non_numeric():
    acc = Account('123456', 1000)
    with pytest.raises(Exception):
        acc.deposit('500')
        acc.deposit(True)

# Test the withdraw method of the Account class with non-numeric amount
def test_account_withdraw_non_numeric():
    acc = Account('123456', 1000)
    with pytest.raises(Exception):
        acc.withdraw('500')
        acc.withdraw(True)

# Test the Account class with concurrent transactions
def test_account_concurrent_transactions():
    acc = Account('123456', 1000)
    acc.deposit(500)
    acc.withdraw(200)
    assert acc.balance == 1300
```
