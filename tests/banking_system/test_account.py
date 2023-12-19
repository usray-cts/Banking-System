import sys
sys.path.insert(0, r'C:\Users\2129823\OneDrive - Cognizant\Documents\Workspace\CapOne Demo\Banking-System\banking_system') 

import pytest
from account import Account

# Test case for creating a new account with a specified account number and initial balance
def test_create_account():
    acc = Account("123456", 5000)
    assert acc.account_number == "123456"
    assert acc.balance == 5000

    acc = Account("7891011", 0)
    assert acc.account_number == "7891011"
    assert acc.balance == 0

# Test case for creating a new account with a specified account number and no initial balance
def test_create_account_no_balance():
    acc = Account("121314")
    assert acc.account_number == "121314"
    assert acc.balance == 0

# Test case for depositing a positive amount into an account
def test_deposit():
    acc = Account("123456", 5000)
    acc.deposit(1000)
    assert acc.balance == 6000

    acc = Account("7891011", 0)
    acc.deposit(500)
    assert acc.balance == 500

# Test case for depositing a zero amount into an account
def test_deposit_zero():
    acc = Account("123456", 5000)
    acc.deposit(0)
    assert acc.balance == 5000

# Test case for depositing a negative amount into an account
def test_deposit_negative():
    acc = Account("123456", 5000)
    with pytest.raises(ValueError):
        acc.deposit(-1000)

# Test case for withdrawing an amount less than or equal to the account balance
def test_withdraw():
    acc = Account("123456", 5000)
    acc.withdraw(1000)
    assert acc.balance == 4000

    acc = Account("7891011", 5000)
    acc.withdraw(5000)
    assert acc.balance == 0

# Test case for withdrawing an amount greater than the account balance
def test_withdraw_insufficient_balance():
    acc = Account("123456", 5000)
    assert acc.withdraw(6000) == "Insufficient balance"

# Test case for withdrawing a zero amount from an account
def test_withdraw_zero():
    acc = Account("123456", 5000)
    acc.withdraw(0)
    assert acc.balance == 5000

# Test case for withdrawing a negative amount from an account
def test_withdraw_negative():
    acc = Account("123456", 5000)
    with pytest.raises(ValueError):
        acc.withdraw(-1000)

# Test case for performing multiple deposits and withdrawals on an account
def test_multiple_operations():
    acc = Account("123456", 5000)
    acc.deposit(1000)
    acc.withdraw(500)
    acc.deposit(2000)
    acc.withdraw(2500)
    assert acc.balance == 5000
