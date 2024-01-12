```python
import pytest
from account import Account

# Unit Test Code

# Test the initialization of the Account class
def test_account_init():
    # Test initialization with no initial balance
    account = Account(123456)
    assert account.account_number == 123456
    assert account.balance == 0

    # Test initialization with an initial balance
    account = Account(123456, 1000)
    assert account.account_number == 123456
    assert account.balance == 1000

# Test the deposit method of the Account class
def test_account_deposit():
    account = Account(123456, 1000)

    # Test depositing a positive amount
    account.deposit(500)
    assert account.balance == 1500

    # Test depositing a zero amount
    account.deposit(0)
    assert account.balance == 1500

    # Test depositing a negative amount (edge case)
    account.deposit(-500)
    assert account.balance == 1000

# Test the withdraw method of the Account class
def test_account_withdraw():
    account = Account(123456, 1000)

    # Test withdrawing an amount less than the balance
    account.withdraw(200)
    assert account.balance == 800

    # Test withdrawing an amount equal to the balance
    account.withdraw(800)
    assert account.balance == 0

    # Test withdrawing an amount greater than the balance
    result = account.withdraw(2000)
    assert result == "Insufficient balance"
    assert account.balance == 0

    # Test withdrawing a negative amount (edge case)
    account.withdraw(-200)
    assert account.balance == 200

# Test checking the balance of the Account class
def test_account_balance():
    account = Account(123456, 1000)

    # Test checking the balance after a deposit
    account.deposit(500)
    assert account.balance == 1500

    # Test checking the balance after a withdrawal
    account.withdraw(200)
    assert account.balance == 1300

    # Test checking the balance after an unsuccessful withdrawal
    account.withdraw(2000)
    assert account.balance == 1300

# Test manipulating multiple accounts
def test_multiple_accounts():
    account1 = Account(123456, 1000)
    account2 = Account(789012, 2000)

    # Test depositing to account1
    account1.deposit(500)
    assert account1.balance == 1500

    # Test withdrawing from account2
    account2.withdraw(1000)
    assert account2.balance == 1000
```