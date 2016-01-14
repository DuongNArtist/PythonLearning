class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

    def __str__(self):
        return 'Point(%d, %d)' % (self.x, self.y)

    def distance_from_origin(self):
        return

    pass


import string

print(string.ascii_letters)
print(string.punctuation)
print(string.printable)
