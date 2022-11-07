def mane_function(n):
    if n == 1:
        return 1
    return n + mane_function(n - 1)

print(mane_function(10))

def linear_search(lys, element):
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1

print(linear_search([1, 2, 3, 4, 5, 2, 1], 2))