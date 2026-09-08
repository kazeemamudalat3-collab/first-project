def remove_duplicate(items):
    new_list = []

    for i in items:
         if i not in new_list:
             new_list.append(i)
    return new_list