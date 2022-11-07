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

def test_function(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print(test_function([10,20,30,40,50,60,70,80,90,100], 20))

