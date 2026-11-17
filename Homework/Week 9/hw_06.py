### TASK 1 ###
# Create a class BankAccount which will keep information of the account holder
# (unique id and name), a 4-digit pin, and the current balance.
# A new bank account starts with zero balance.
# Provide methods to deposit(amount) which will add to the balance,
# taking care to accept only positive values, withdraw(amount) to get money
# and subtract from the balance - taking care to accept amounts within the balance limit,
# and get_balance() to view current balance.Test the class to check correctness.

class BankAccount:
    def __init__(self, account_id, name, pin):
        self.account_id = account_id
        self.name = name
        self.pin = pin
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"New Balance: ${self.balance}")
        else:
            print("Withdrawal amount must be positive and within the balance limit.")

    def get_balance(self):
        return self.balance


### TASK 2 ###
# Create a class ATM which will keep a list or dictionary (whatever you find more convenient) of BankAccount objects.
# The ATM will provide initially a prompt to login:
# ID: <user types their id>
# PIN: <user types their pin>
# If both, id and pin, match with the stored in the account a menu will appear:
# 1. Deposit
# 2. Withdraw
# 3. View Balance
# 0. Exit
# Select >
# Selecting a value between 1 and 3, provide the respective functionality.

class ATM:
    def __init__(self):
        self.accounts = {}

    def display_prompt(self):
        account_id = input("ID: ")
        pin = input("PIN: ")

        if account_id in self.accounts and self.accounts[account_id].pin == pin:
            self.display_menu(self.accounts[account_id])
        else:
            print("Invalid ID or PIN.")

    def display_menu(self, account):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. View Balance")
            print("0. Exit")
            choice = input("Select > ")

            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == '3':
                print(f"Current Balance: ${account.get_balance()}")
            elif choice == '0':
                break
            else:
                print("Invalid selection. Please try again.")
