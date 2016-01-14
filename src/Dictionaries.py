# Bundling information
dd = dict(
        name='duong nguyen',
        language='python',
        location='vietnamese'
)
print(dd)
# From list to dictionary
rank_list = ['the', 'be', 'of', 'and', 'a', 'in', 'to', 'have', 'it', 'to', 'for', 'I', 'that', 'you', 'he', 'on',
             'with', 'do', 'at', 'by', 'not', 'this', 'but', 'from', 'they', 'his', ...]
rank_dict = dict()
for (i, word) in enumerate(rank_list):
    rank_dict[word] = (i + 1)
    pass
print(rank_dict)

# Zip
from string import ascii_lowercase

print(ascii_lowercase)
my_range = range(1, 27)
print(my_range)
my_zip = zip(ascii_lowercase, my_range)
print(my_zip)
my_dict = dict(my_zip)
print(my_dict)
