def group_by_category(items):
    grouped = {}
   

    for item, category in items:
        if category not in grouped:
             grouped[category] = []
        grouped[category].append(item)
            
            

    return grouped

items = [
    ("apple", "fruit"),
    ("carrot", "vegetable"),
    ("banana", "fruit"),
    ("spinach", "vegetable"),
    ("orange", "fruit")
]

print(group_by_category(items))