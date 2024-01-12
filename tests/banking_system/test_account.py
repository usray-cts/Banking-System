```python
import pytest
from account import Account

def test_account_initialization():
    # Test initialization with specific account number and initial balance
    acc1 = Account(123456, 1000)
    assert acc1.account_number == 123456
    assert acc1.balance == 1000

    # Test initialization with specific account number and no initial balance
    acc2 = Account(789012)
    assert acc2.account_number == 789012
    assert acc2.balance == 0

def test_deposit():
    acc = Account(123456, 1000)

    # Test depositing a positive amount of money
    assert acc.deposit(500) == 1500

    # Test depositing a zero amount of money
    assert acc.deposit(0) == 1500

    # Test attempting to deposit a negative amount of money
    with pytest.raises(ValueError):
        acc.deposit(-500)

def test_withdraw():
    acc = Account(123456, 1500)

    # Test withdrawing an amount less than the balance
    assert acc.withdraw(500) == 1000

    # Test withdrawing an amount equal to the balance
    assert acc.withdraw(1000) == 0

    # Test attempting to withdraw an amount greater than the balance
    assert acc.withdraw(500) == "Insufficient balance"

    # Test attempting to withdraw a negative amount
    with pytest.raises(ValueError):
        acc.withdraw(-500)

def test_edge_cases():
    acc = Account(123456, 0)

    # Test withdrawing or depositing extremely large amounts
    assert acc.deposit(1e18) == 1e18
    assert acc.withdraw(1e18) == 0

    # Test handling of decimal amounts
    assert acc.deposit(0.1) == 0.1
    assert acc.withdraw(0.05) == 0.05

def test_other_scenarios():
    acc1 = Account(123456, 1000)
    acc2 = Account(789012, 2000)

    # Test checking the balance after various transactions
    acc1.deposit(500)
    acc1.withdraw(200)
    assert acc1.balance == 1300

    # Test interaction between multiple account objects
    acc2.deposit(acc1.withdraw(300))
    assert acc1.balance == 1000
    assert acc2.balance == 2300
```