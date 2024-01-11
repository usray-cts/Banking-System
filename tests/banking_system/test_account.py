```python
import pytest
from account import Account

# Unit tests for the Account class
class TestAccount:
    # Test initialization of Account
    def test_init(self):
        account = Account('1234567890')
        assert account.account_number == '1234567890'
        assert account.balance == 0

        account = Account('1234567890', 1000)
        assert account.account_number == '1234567890'
        assert account.balance == 1000

    # Test deposit transactions
    def test_deposit(self):
        account = Account('1234567890')
        assert account.deposit(500) == 500
        assert account.balance == 500

        assert account.deposit(0) == 500
        assert account.balance == 500

        with pytest.raises(ValueError):
            account.deposit(-500)

    # Test withdrawal transactions
    def test_withdraw(self):
        account = Account('1234567890', 1000)
        assert account.withdraw(200) == 800
        assert account.balance == 800

        assert account.withdraw(800) == 0
        assert account.balance == 0

        assert account.withdraw(0) == 0
        assert account.balance == 0

        assert account.withdraw(1500) == "Insufficient balance"
        assert account.balance == 0

        with pytest.raises(ValueError):
            account.withdraw(-200)
```