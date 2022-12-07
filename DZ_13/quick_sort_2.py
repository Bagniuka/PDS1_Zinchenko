import time
import random

my_list = []
for i in range(0, 5000):
    my_list.append(random.randint(1, 1000))
print("Sorting List:", my_list)

start = time.perf_counter()

def quick_sort(s):
    if len(s) <= 1:
        return s
    pivot = s[0]
    left = list(filter(lambda x: x < pivot, s))
    center = [i for i in s if i == pivot]
    right = list(filter(lambda x: x > pivot, s))

    return quick_sort(left) + center + quick_sort(right)

finish = time.perf_counter()

print(quick_sort(my_list))
print(finish - start)