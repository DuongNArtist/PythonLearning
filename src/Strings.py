separator = " "
string = "Hello! It's me. Hello! How are you"

split_array = string.split(separator)
print(split_array)

join_string = separator.join(split_array)
print(join_string)

string.capitalize()
print(string)

string_count = "Hello"
print("Number of times", string_count, "appears in the string", string, "is", string.count(string_count))

string_index = "me"
print("Index of ", string_index, "is", string.index(string_index))

string_find = "Hello"
print("First index of", string_find, "in", string, "is", string.find(string_find))

string_rfind = "Hello"
print("Last index of", string_rfind, "in", string, "is", string.rfind(string_rfind))

string_replace = "I"
print(string.replace("me", string_replace))

# strip copy of s without leading or trailing whitespace
print(string.strip("u"))

# S.title() Return a string just like S in which all words are capitalized:
print(string.title())
