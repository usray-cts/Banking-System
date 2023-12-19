import sys
sys.path.insert(0, r'C:\Users\2129823\OneDrive - Cognizant\Documents\Workspace\CapOne Demo\Banking-System\banking_system') 

import pytest
from unittest.mock import Mock
from account import Account
from  transaction import Transaction



def test_deposit():
    # Test normal operation
    account = Account("12345678", 0)
    transaction = Transaction(account)
    transaction.deposit(500)
    assert account.balance == 500

    # Test depositing negative amount
    with pytest.raises(ValueError):
        transaction.deposit(-500)

    # Test depositing non-numeric amount
    with pytest.raises(TypeError):
        transaction.deposit("five hundred")

def test_withdraw():
    # Test normal operation
    account = Account("12345678", 500)
    transaction = Transaction(account)
    transaction.withdraw(200)
    assert account.balance == 300

    # Test withdrawing more than balance
    with pytest.raises(ValueError):
        transaction.withdraw(400)

    # Test withdrawing negative amount
    with pytest.raises(ValueError):
        transaction.withdraw(-200)

    # Test withdrawing non-numeric amount
    with pytest.raises(TypeError):
        transaction.withdraw("two hundred")

def test_large_inputs():
    # Test large deposit
    account = Account("12345678", 0)
    transaction = Transaction(account)
    transaction.deposit(1000000000)
    assert account.balance == 1000000000

    # Test large withdrawal
    account = Account("12345678", 2000000000)
    transaction = Transaction(account)
    transaction.withdraw(1000000000)
    assert account.balance == 1000000000

def test_invalid_account():
    # Test invalid account number
    with pytest.raises(ValueError):
        account = Account("123", 0)

    # Test non-numeric account number
    with pytest.raises(ValueError):
        account = Account("123abc", 0)

if __name__ == "__main__":
    pytest.main()
