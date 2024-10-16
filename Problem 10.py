class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds!")
    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
account.withdraw(300)
print(account.get_balance())
account.withdraw(1500)