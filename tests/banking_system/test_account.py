```python
import pytest
from account import Account

# Unit tests for Account class

def test_account_initialization():
    # Test initialization with positive balance
    account = Account('12345678', 1000)
    assert account.account_number == '12345678'
    assert account.balance == 1000

    # Test initialization with zero balance
    account = Account('12345678', 0)
    assert account.account_number == '12345678'
    assert account.balance == 0

    # Test initialization without specifying balance
    account = Account('12345678')
    assert account.account_number == '12345678'
    assert account.balance == 0

def test_deposit():
    # Test depositing positive amount
    account = Account('12345678', 1000)
    assert account.deposit(500) == 1500

    # Test depositing zero amount
    assert account.deposit(0) == 1500

    # Test depositing negative amount
    assert account.deposit(-500) == 1000

def test_withdraw():
    # Test withdrawing amount less than balance
    account = Account('12345678', 1000)
    assert account.withdraw(500) == 500

    # Test withdrawing amount equal to balance
    assert account.withdraw(500) == 0

    # Test withdrawing amount greater than balance
    assert account.withdraw(1500) == "Insufficient balance"

    # Test withdrawing negative amount
    assert account.withdraw(-500) == "Insufficient balance"

def test_multiple_transactions():
    # Test multiple transactions in sequence
    account = Account('12345678', 1000)
    assert account.deposit(500) == 1500
    assert account.withdraw(400) == 1100
    assert account.deposit(300) == 1400
    assert account.withdraw(200) == 1200

    # Test multiple transactions resulting in insufficient balance
    account = Account('12345678', 1000)
    assert account.deposit(500) == 1500
    assert account.withdraw(1500) == 0
    assert account.withdraw(500) == "Insufficient balance"
```
