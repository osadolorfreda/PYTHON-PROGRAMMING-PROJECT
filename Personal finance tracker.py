class Transaction:
    def __init__(self, amount, type, category):
        self.amount = amount
        self.type = type
        self.category = category

class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.budget = {}

    def add_transaction(self):
        amount = float(input("Enter the amount of money: "))
        type = input("Enter the type of transaction (income/expense): ")
        category = input("Enter the category of transaction: ")
        transaction = Transaction(amount, type, category)
        self.transactions.append(transaction)

    def view_transactions(self):
        for transaction in self.transactions:
            print(f"Amount: {transaction.amount}, Type: {transaction.type}, Category: {transaction.category}")

    def calculate_balance(self):
        income = sum(t.amount for t in self.transactions if t.type == 'income')
        expense = sum(t.amount for t in self.transactions if t.type == 'expense')
        total = income - expense
        print(f"Balance: {total}")

    def set_budget(self):
        category = input("Enter the category of transaction: ")
        budget = float(input("Enter the budget: "))
        self.budget[category] = budget

    def check_budget(self):
        for category, budget in self.budget.items():
            spent = sum(t.amount for t in self.transactions if t.category == category and t.type == 'expense')
            print(f"Category: {category}, Budget: {budget}, Spent: {spent}")

class CurrencyConverter:
    rates = {'USD': 1, 'EUR': 0.9, 'GBP': 0.8}  # Example rates

    def convert_currency(self, amount, to_currency):
        if to_currency in self.rates:
            return amount * self.rates[to_currency]
        else:
            print("Invalid Currency")
            return None

def main():
    tracker = FinanceTracker()
    converter = CurrencyConverter()

    while True:
        print("\nWelcome to Finance Tracker")
        print("1. Add transaction\n2. View transactions\n3. Calculate balance\n4. Set budget\n5. Check budget\n6. Currency converter\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            tracker.add_transaction()
        elif choice == '2':
            tracker.view_transactions()
        elif choice == '3':
            tracker.calculate_balance()
        elif choice == '4':
            tracker.set_budget()
        elif choice == '5':
            tracker.check_budget()
        elif choice == '6':
            amount = float(input("Enter amount: "))
            to_currency = input("Enter currency (USD/EUR/GBP): ")
            converted = converter.convert_currency(amount, to_currency)
            if converted:
                print(f"Converted amount: {converted}")
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()