def cross(rows, cols):
    return [r + c for r in rows for c in cols]
    pass


print(cross('ABC', '123'))
