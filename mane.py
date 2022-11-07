def mane_function(n):
    if n == 1:
        return 1
    return n + mane_function(n - 1)

print(mane_function(10))

def test_function(lys, val):
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