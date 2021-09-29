'''
Create a Budget class that can instantiate objects based on different
budget categories like food, clothing, and entertainment. These objects
should allow for depositing and withdrawing funds from each category,
as well computing category balances and transferring balance amounts 
between categories.
'''

class Budget():
    def move(budget1, category1, budget2, category2, amount):
        budget1.withdraw(category1, amount)
        budget2.deposit(category2, amount)
    
    def __init__(self, food, clothing, entertainment, utilities, rent):
        self.clothing = clothing
        self.food = food
        self.entertainment = entertainment
        self.utilities = utilities
        self.rent = rent
        self.total = self.clothing + self.food + self.entertainment + self.utilities + self.rent
    
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
        return f"-----\nTotal budget is {self.total}.\nEntertainment: {(self.entertainment/self.total)*100:.2f}%\nFood: {(self.food/self.total)*100:.2f}%\nClothing: {(self.clothing/self.total)*100:.2f}%\nUtilities: {(self.utilities/self.total)*100:.2f}%\nRent: {(self.rent/self.total)*100:.2f}%\n-----"
        

# Example usage
budget = Budget(100, 50, 100, 200, 300)
budget.deposit("Entertainment", 20)
budget.withdraw("rent", 50)
budget.transfer("entertainment", "rent", 50)
print(budget)
newbudget = Budget(50, 30, 20, 100, 200)
Budget.move(budget, "rent", newbudget, "food", 30)
print(newbudget)