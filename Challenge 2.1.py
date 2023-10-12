class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"{self.__account_holder_name} deposited ₹{amount}. New balance is ₹{self.__account_balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"{self.__account_holder_name} withdrew ₹{amount}. New balance is ₹{self.__account_balance}")
        else:
            print("Withdrawal amount exceeds account balance. Transaction Failed.")

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name} (Account number: {self.__account_number}) is: ₹{self.__account_balance}"

# Creating an instance of BankAccount
my_account = BankAccount("12345", "Kavitha", 1000)
print(my_account.display_balance())

# Depositing money
my_account.deposit(500)

# Withdrawing money
my_account.withdraw(200)

# Attempt to withdraw (insufficient funds)
my_account.withdraw(2000)

# Displaying the account balance
print(my_account.display_balance())