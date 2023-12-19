from account import Account
from transaction import Transaction

def main():
    account = Account("12345678",0)
    transaction = Transaction(account)

    print(transaction.deposit(500))
    print(transaction.withdraw(200))
    print(transaction.withdraw(400))

if __name__ == "__main__":
    main()
