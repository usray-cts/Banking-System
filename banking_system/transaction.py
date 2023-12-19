from account import Account

class Transaction:
    def __init__(self, account: Account):
        self.account = account

    def deposit(self, amount):
        new_balance = self.account.deposit(amount)
        return f"Deposit successful. New balance is {new_balance}"

    def withdraw(self, amount):
        result = self.account.withdraw(amount)
        if type(result) == str:
            return result
        else:
            return f"Withdrawal successful. New balance is {result}"
