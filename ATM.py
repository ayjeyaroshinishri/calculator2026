
class ATM:
    def __init__(self, initial_balance=0.0, pin="1234"):
        self.balance = float(initial_balance)
        self.pin = pin
        self.is_authenticated = False
        self.transactions = []  # store tuples like ("deposit", amount)

    def authenticate(self, entered_pin):
        if entered_pin == self.pin:
            self.is_authenticated = True
            print("Authentication successful.")
        else:
            print("Invalid PIN. Try again.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transactions.append(("deposit", amount))
        print(f"Deposited ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.transactions.append(("withdraw", amount))
        print(f"Withdrew ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
    
    # Add this method inside the ATM class
    def mini_statement(self, limit=5):            #merge content
        if not self.transactions:
            print("No transactions yet.")
            return
        print(f"Last {min(limit, len(self.transactions))} transactions:")
        for t_type, amount in self.transactions[-limit:]:
            print(f"- {t_type.capitalize()}: ₹{amount:.2f}")

def main():
    atm = ATM(initial_balance=1000.0, pin="4321")
    print("Welcome to the ATM")
    for _ in range(3):
        entered_pin = input("Enter PIN: ").strip()
        atm.authenticate(entered_pin)
        if atm.is_authenticated:
            break
    if not atm.is_authenticated:
        print("Too many failed attempts. Exiting.")
        return

    while True:
        print("\nSelect an option:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Mini Statement")
        print("5. Exit")
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))
                atm.deposit(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == "4":
            atm.mini_statement()
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()