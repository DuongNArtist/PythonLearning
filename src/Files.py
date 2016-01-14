import codecs

file_name = 'document.txt'
with codecs.open(file_name, 'r', encoding='utf8') as file:
    text = file.read()
    pass
print(text)

from collections import Counter

words = str(text).split(' ')
counter = Counter()
for word in words:
    counter[word] += 1
    pass
print(counter)
print(counter.most_common(3))
print(counter.values())
