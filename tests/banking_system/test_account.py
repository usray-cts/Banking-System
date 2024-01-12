```python
import pytest
from account import Account

# Unit tests for the Account class

def test_account_initialization():
    # Test initializing an account with only an account number
    account = Account('12345678')
    assert account.account_number == '12345678'
    assert account.balance == 0

    # Test initializing an account with an account number and a balance
    account = Account('12345678', 1000)
    assert account.account_number == '12345678'
    assert account.balance == 1000

def test_deposit():
    # Test depositing a positive amount of money
    account = Account('12345678')
    account.deposit(500)
    assert account.balance == 500

    # Test depositing a zero amount of money
    account.deposit(0)
    assert account.balance == 500

    # Test depositing a negative amount of money
    with pytest.raises(ValueError):
        account.deposit(-500)

def test_withdraw():
    # Test withdrawing an amount of money that is less than the balance
    account = Account('12345678', 1000)
    account.withdraw(500)
    assert account.balance == 500

    # Test withdrawing an amount of money that is equal to the balance
    account.withdraw(500)
    assert account.balance == 0

    # Test withdrawing an amount of money that is greater than the balance
    with pytest.raises(ValueError):
        account.withdraw(1500)

def test_balance_check():
    # Test checking the balance when it is positive
    account = Account('12345678', 1000)
    assert account.balance == 1000

    # Test checking the balance when it is zero
    account = Account('12345678')
    assert account.balance == 0

    # Test checking the balance when it is negative
    with pytest.raises(ValueError):
        account = Account('12345678', -500)

# Edge Cases
def test_non_numeric_initialization():
    # Test initializing an account with a non-numeric account number
    with pytest.raises(ValueError):
        account = Account('abc123')

def test_non_numeric_deposit():
    # Test depositing a non-numeric amount of money
    account = Account('12345678')
    with pytest.raises(ValueError):
        account.deposit('500')

def test_non_numeric_withdraw():
    # Test withdrawing a non-numeric amount of money
    account = Account('12345678', 1000)
    with pytest.raises(ValueError):
        account.withdraw('500')
```