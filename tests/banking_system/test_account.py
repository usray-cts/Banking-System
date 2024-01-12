```python
import pytest
from account import Account

# Unit tests for the Account class
class TestAccount:

    # Test for creating an account
    def test_create_account(self):
        account = Account('123456', 500)
        assert account.account_number == '123456'
        assert account.balance == 500

        account = Account('123456', 0)
        assert account.account_number == '123456'
        assert account.balance == 0

        account = Account('123456')
        assert account.account_number == '123456'
        assert account.balance == 0

    # Test for depositing money
    def test_deposit(self):
        account = Account('123456', 500)
        assert account.deposit(500) == 1000
        assert account.deposit(0) == 1000

        with pytest.raises(ValueError):
            account.deposit(-500)

    # Test for withdrawing money
    def test_withdraw(self):
        account = Account('123456', 1000)
        assert account.withdraw(200) == 800
        assert account.withdraw(800) == 0
        assert account.withdraw(700) == 'Insufficient balance'

        with pytest.raises(ValueError):
            account.withdraw(-200)

    # Test for edge cases
    def test_edge_cases(self):
        with pytest.raises(ValueError):
            Account('123456', 'five hundred')

        with pytest.raises(ValueError):
            Account(123456, 500)
```
