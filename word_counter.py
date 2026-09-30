sentence = input("Enter your sentence: ")
count = {}
words = sentence.split()
for word in words:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1

    
print(count)