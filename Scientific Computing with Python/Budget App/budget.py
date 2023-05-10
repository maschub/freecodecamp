class Category:
    def __init__(self, name):
        self.ledger = []
        self.balance = 0.0
        self.name = name

    def __str__(self):
        output = str(self.name).center(30, "*")
        for line in self.ledger:
            amount = f"{line['amount']:.2f}"
            output = f"{output}\n{line['description'][:23].ljust(23,' ')}{amount.rjust(7)}"

        output = f"{output}\nTotal: {self.balance:.2f}"
        return output

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({
                "amount": amount*-1,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other_category):
        if self.withdraw(amount, f"Transfer to {other_category.name}"):
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return float(amount) <= self.balance


def create_spend_chart(categories):
    output = "Percentage spent by category"
    expenses = {}
    longest_cat = 0
    for category in categories:
        category_sum = 0
        if len(category.name) > longest_cat:
            longest_cat = len(category.name)
        for item in category.ledger:
            if item['amount'] < 0:
                category_sum += item['amount']
        expenses[category.name] = round(category_sum, 2)
    expenses_sum = sum(expenses.values())
    for i in range(100, -10, -10):
        output = f"{output}\n{str(i).rjust(3)}|"
        for value in expenses.values():
            if value / expenses_sum * 100 >= i:
                output = f"{output} o "
            else:
                output = f"{output}   "
        output = f"{output} "
    output = f"{output}\n    {''.rjust(len(categories)*3+1, '-')}"
    for char in range(0, longest_cat):
        output = f"{output}\n    "
        for category in categories:
            try:
                output = f"{output}{category.name[char].center(3)}"
            except IndexError:
                output = f"{output}   "
        output = f"{output} "

    return output
