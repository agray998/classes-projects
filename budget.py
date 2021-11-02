'''
Create a Budget class that can instantiate objects based on different
budget categories like food, clothing, and entertainment. These objects
should allow for depositing and withdrawing funds from each category,
as well computing category balances and transferring balance amounts 
between categories.
'''

class Budget():
    @staticmethod
    def move(budget1, category1, budget2, category2, amount):
        budget1.withdraw(category1, amount)
        budget2.deposit(category2, amount)
    
    def __init__(self, dict_of_cats):
        self.cats = dict_of_cats.keys()
        for key in dict_of_cats.keys():
            setattr(self, key, dict_of_cats[key])
        self.total = sum(dict_of_cats.values())
    
    def deposit(self, category, amount):
        self.total += amount
        amount += getattr(self, category.lower())
        setattr(self, category.lower(), amount)
        print(f"{category.capitalize()} budget is now {amount}")

    def withdraw(self, category, amount):
        self.total -= amount
        currentBal = getattr(self, category.lower())
        setattr(self, category.lower(), currentBal - amount)
        print(f"{category.capitalize()} budget is now {currentBal - amount}")
    
    def transfer(self, category1, category2, amount):
        print(f"Transferred {amount} from {category1.capitalize()} to {category2.capitalize()}")
        self.withdraw(category1, amount)
        self.deposit(category2, amount)
    
    def __repr__(self):
        newline = '\n'
        return f"""-----\nTotal budget is {self.total}.\n{newline.join([f"{cat.capitalize()}: {getattr(self, cat) / self.total * 100:.2f}%" for cat in self.cats])}\n-----"""

# Example usage
budget = Budget({'food':100, 'clothing':50, 'entertainment':100, 'utilities':200, 'rent':300})
budget.deposit("Entertainment", 20)
budget.withdraw("rent", 50)
budget.transfer("entertainment", "rent", 50)
print(budget)
newbudget = Budget({'food':50, 'clothing':30, 'entertainment':20, 'utilities':100, 'rent':200})
Budget.move(budget, "rent", newbudget, "food", 30)
print(newbudget)