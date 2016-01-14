from collections import Counter

counter = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    counter[word] += 1
    pass
print(counter)
