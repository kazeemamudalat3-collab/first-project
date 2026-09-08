def most_frequent(items):
    counts = {}

    for item in items:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1
    
# If this is the first time I've seen it, start at 1. Otherwise add to it 
    highest_count = 0
    most_commom = None
    for item in counts:
        if counts[item] > highest_count:
            highest_count = counts[item]
            # when you find a higher count, you need to remember which item had that count
            most_commom = item
    return most_commom  
        
print(most_frequent([1, 2, 2, 3, 2, 4, 1]))