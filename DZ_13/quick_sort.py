import time
import random

my_list = []
for i in range(0, 5000):
    my_list.append(random.randint(1, 1000))
print("Sorting List:", my_list)

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


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)


cur_time = time.time()
quick_sort(my_list)
print("Quick Sort:", my_list)
print(f"Duration time: {time.time() - cur_time}")