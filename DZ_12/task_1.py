import concurrent.futures
import time

# Calculate factorial function
def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


if __name__ == '__main__':
    # ThreadPoolExecutor speed test
    start1 = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        numbers = [_ for _ in range(1, 10)]
        results = [executor.submit(factorial, num) for num in numbers]

    for result in results:
        print(result.result())

    finish1 = time.perf_counter()

    time_result1 = finish1 - start1
    print(f"Time to execut: {time_result1} seconds\n")


    # ProcessPoolExecutor speed test
    start2 = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        numbers = [_ for _ in range(1, 10)]
        results = [executor.submit(factorial, num) for num in numbers]

    for result in results:
        print(result.result())

    finish2 = time.perf_counter()

    time_result2 = finish2 - start2
    print(f"Time to execut: {time_result2} seconds")


    # Time speed comparison
    if time_result1 < time_result2:
        print(f'\nThe best method is ThreadPoolExecutor.\nIt tooks {time_result2 - time_result1} less seconds to execute!')

    if time_result2 < time_result1:
        print(f'\nThe best method is ProcessPoolExecutor.\nIt tooks {time_result1 - time_result2} less seconds to execute!')