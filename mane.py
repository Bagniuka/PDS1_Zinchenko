def mane_function(n):
    if n == 1:
        return 1
    return n + mane_function(n - 1)

print(mane_function(10))