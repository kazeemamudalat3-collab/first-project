def count_unique(items):
    count = 0
    counted_list = []
    for i in items:
        if i not in counted_list:
            count += 1
            counted_list.append(i)
    return count

# print(count_unique([1, 2, 2, 3, 1, 4]))