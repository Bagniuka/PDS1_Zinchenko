import time
import random
from random_words import RandomWords

w = RandomWords()

int_list = []
float_list = []
str_list = []

# Randomizer
start_randomizer = time.perf_counter()

for _ in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.random_word())

finish_randomizer = time.perf_counter()
print(f'Randomizer done in {finish_randomizer - start_randomizer} seconds.')


# Bubble sorting
def bubble_sort(list, iter_ammount):
    total_time = []
    for _ in range(iter_ammount):
        start = time.perf_counter()
        length = len(list)
        for iIndex in range(length):
            for jIndex in range(0, length - iIndex - 1):
                if list[jIndex] > list[jIndex + 1]:
                    list[jIndex], list[jIndex + 1] = list[jIndex + 1], list[jIndex]

        finish = time.perf_counter()
        one_iter_time = finish - start
        total_time.append(one_iter_time)
    print(f'Average time of {iter_ammount} Bubble sorting iterations is {sum(total_time) / len(total_time)} second(s).')


# Quick sorting
def quick_sort(list, iter_ammount):
    total_time = []
    for _ in range(iter_ammount):
        start = time.perf_counter()
        def _quick_sort(items, low, high):
            if low < high:
                split_index = partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(list, 0, len(list) - 1)

        finish = time.perf_counter()
        one_iter_time = finish = start
        total_time.append(one_iter_time)
    print(f'Average time of {iter_ammount} Quick sorting iterations is {sum(total_time) / len(total_time)} second(s).')

def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


# Insertion sorting
def insertion_sort(list, iter_ammount):
    total_time = []
    for _ in range(iter_ammount):
        start = time.perf_counter()
        for scanIndex in range(1, len(list)):
            tmp = list[scanIndex]
            minIndex = scanIndex
            while minIndex > 0 and tmp < list[minIndex - 1]:
                list[minIndex] = list[minIndex - 1]
                minIndex -= 1
            list[minIndex] = tmp

        finish = time.perf_counter()
        one_iter_time = finish - start
        total_time.append(one_iter_time)
    print(f'Average time of {iter_ammount} Insertion sorting iterations is {sum(total_time) / len(total_time)} second(s).')


bubble_sort(int_list, 10)
quick_sort(float_list, 10)
insertion_sort(str_list, 10)
