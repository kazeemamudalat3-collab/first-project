# Store expenses in a dictionary and calculate:
# Total spending
# Spending by category
# Highest expense
# Average expense


# expenses = {
#     "food": 5000,
#     "transport": 3000,
#     "internet": 5000,
#     "food": 2500
# }
     
    
# Store expenses in a dictionary.
# Each category has a list so we can store multiple expenses
# under the same category.

expenses = {
    "food": [5000, 2500],
    "transport": [3000],
    "internet": [5000]
}


# 1. Calculate total spending

total = 0

for category, amounts in expenses.items():
    total += sum(amounts)

print(f"Your total expense is {total}")


# 2. Spending by category

print("\nSpending by category:")

for category, amounts in expenses.items():
    print(f"{category}: {sum(amounts)}")


# 3. Get all individual expenses

all_expenses = []

for amounts in expenses.values():
    all_expenses.extend(amounts)


# 4. Find highest expense

highest = max(all_expenses)

print(f"\nHighest expense is {highest}")


# 5. Calculate average expense

average = sum(all_expenses) / len(all_expenses)

print(f"Average expense is {average}")   