#!/usr/bin/python3
class Checkbook:
    """
    Class representing a simple checkbook with deposit, withdrawal, and balance checking.
    """
    def __init__(self):
        """
        Initializes a new checkbook with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Parameters:
            amount (float): the amount to deposit.

        Effect:
            Increases the account balance and prints the deposit and current balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds exist.

        Parameters:
            amount (float): the amount to withdraw.

        Effect:
            - If the balance is sufficient, decreases the balance and prints the withdrawal and current balance.
            - Otherwise, prints an error message.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current account balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function allowing the user to interact with the checkbook
    via a command-line interface.
    Available commands: deposit, withdraw, balance, exit
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action == 'exit':
            print("Goodbye!")
            break
        elif action == 'deposit':
            while True :
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    if amount <= 0:
                        print("Please enter a positive amount.")
                        continue
                    cb.deposit(amount)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif action == 'withdraw':
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    if amount <= 0:
                        print("Please enter a positive amount.")
                        continue
                    cb.withdraw(amount)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()