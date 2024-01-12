```python
import pytest
from account import Account

def test_account_initialization():
    # Test case: Creating an account with a specific account number and no initial balance.
    account1 = Account(123456)
    assert account1.account_number == 123456
    assert account1.balance == 0

    # Test case: Creating an account with a specific account number and an initial balance.
    account2 = Account(234567, 1000)
    assert account2.account_number == 234567
    assert account2.balance == 1000

def test_deposit():
    account = Account(123456, 1000)

    # Test case: Depositing a positive amount into the account.
    account.deposit(500)
    assert account.balance == 1500

    # Test case: Depositing zero into the account.
    account.deposit(0)
    assert account.balance == 1500

    # Edge case: Attempting to deposit a negative amount.
    with pytest.raises(ValueError):
        account.deposit(-500)

def test_withdraw():
    account = Account(123456, 1000)

    # Test case: Withdrawing an amount less than the balance.
    account.withdraw(500)
    assert account.balance == 500

    # Test case: Withdrawing an amount equal to the balance.
    account.withdraw(500)
    assert account.balance == 0

    # Edge case: Withdrawing an amount greater than the balance.
    assert account.withdraw(500) == "Insufficient balance"
    assert account.balance == 0

    # Edge case: Attempting to withdraw a negative amount.
    with pytest.raises(ValueError):
        account.withdraw(-500)

def test_account_number_edge_cases():
    # Edge case: Creating an account with a non-numeric account number.
    with pytest.raises(ValueError):
        Account("123abc")

    # Edge case: Creating an account with a negative account number.
    with pytest.raises(ValueError):
        Account(-123456)

def test_balance_edge_cases():
    # Edge case: Creating an account with a non-numeric balance.
    with pytest.raises(ValueError):
        Account(123456, "1000")

    # Edge case: Creating an account with a negative balance.
    with pytest.raises(ValueError):
        Account(123456, -1000)
```