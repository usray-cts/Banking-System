```python
import pytest
from account import Account

# Step1: Test initialization of the account
def test_account_initialization():
    account = Account('123456', 1000)
    assert account.account_number == '123456'
    assert account.balance == 1000

    account = Account('123456')
    assert account.balance == 0

# Step2: Test deposit method
def test_deposit():
    account = Account('123456', 1000)
    account.deposit(500)
    assert account.balance == 1500

    account.deposit(0)
    assert account.balance == 1500

    with pytest.raises(ValueError):
        account.deposit(-500)

# Step3: Test withdraw method with sufficient balance
def test_withdraw_sufficient_balance():
    account = Account('123456', 1000)
    account.withdraw(500)
    assert account.balance == 500

    account.withdraw(500)
    assert account.balance == 0

# Step4: Test withdraw method with insufficient balance
def test_withdraw_insufficient_balance():
    account = Account('123456', 500)
    result = account.withdraw(1000)
    assert result == "Insufficient balance"
    assert account.balance == 500

    with pytest.raises(ValueError):
        account.withdraw(-500)

# Step5: Test edge cases
def test_edge_cases():
    account = Account('123456', 1000)
    account.deposit(1.5)
    assert account.balance == 1001.5

    result = account.withdraw(1002.5)
    assert result == "Insufficient balance"
    assert account.balance == 1001.5

# Step6: Test function's behavior with different data types
def test_different_data_types():
    account = Account('123456', 1000)

    with pytest.raises(TypeError):
        account.deposit("500")

    with pytest.raises(TypeError):
        account.withdraw("500")

    with pytest.raises(TypeError):
        Account('123456', "1000")
```