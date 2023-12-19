import sys
sys.path.insert(0, r'C:\Users\2129823\OneDrive - Cognizant\Documents\Workspace\CapOne Demo\Banking-System\banking_system') 

import pytest
from unittest.mock import MagicMock, patch
from account import Account
from transaction import Transaction

# Test the deposit method
def test_deposit():
    # Mock the Account class
    account = MagicMock(Account)
    account.deposit.return_value = 100
    transaction = Transaction(account)

    # Test deposit
    assert transaction.deposit(100) == "Deposit successful. New balance is 100"
    account.deposit.assert_called_once_with(100)

# Test the withdraw method
def test_withdraw():
    # Mock the Account class
    account = MagicMock(Account)
    account.withdraw.return_value = 50
    transaction = Transaction(account)

    # Test withdraw
    assert transaction.withdraw(50) == "Withdrawal successful. New balance is 50"
    account.withdraw.assert_called_once_with(50)

# Test the withdraw method with insufficient funds
def test_withdraw_insufficient_funds():
    # Mock the Account class
    account = MagicMock(Account)
    account.withdraw.return_value = "Insufficient funds"
    transaction = Transaction(account)

    # Test withdraw
    assert transaction.withdraw(150) == "Insufficient funds"
    account.withdraw.assert_called_once_with(150)

# Test the deposit method with negative amount
def test_deposit_negative_amount():
    # Mock the Account class
    account = MagicMock(Account)
    account.deposit.return_value = "Invalid amount"
    transaction = Transaction(account)

    # Test deposit
    assert transaction.deposit(-100) == "Invalid amount"
    account.deposit.assert_called_once_with(-100)

# Test the deposit method with non-numeric amount
def test_deposit_non_numeric_amount():
    # Mock the Account class
    account = MagicMock(Account)
    account.deposit.return_value = "Invalid amount"
    transaction = Transaction(account)

    # Test deposit
    assert transaction.deposit("abc") == "Invalid amount"
    account.deposit.assert_called_once_with("abc")

# Test the withdraw method with non-numeric amount
def test_withdraw_non_numeric_amount():
    # Mock the Account class
    account = MagicMock(Account)
    account.withdraw.return_value = "Invalid amount"
    transaction = Transaction(account)

    # Test withdraw
    assert transaction.withdraw("abc") == "Invalid amount"
    account.withdraw.assert_called_once_with("abc")

# Test the withdraw method with negative amount
def test_withdraw_negative_amount():
    # Mock the Account class
    account = MagicMock(Account)
    account.withdraw.return_value = "Invalid amount"
    transaction = Transaction(account)

    # Test withdraw
    assert transaction.withdraw(-50) == "Invalid amount"
    account.withdraw.assert_called_once_with(-50)
