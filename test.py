import time

def find_number_position(numbers, target):
    start_time = time.time()
    for i, number in enumerate(numbers):
        if number == target:
            end_time = time.time()
            print(f"Execution Time: {end_time - start_time:.10f} seconds")
            return i
    return -1  # If the target is not found, return -1 or handle accordingly

numbers = [12, 34, 68, 45, 68, 89]
target_number = 68
result = find_number_position(numbers, target_number)
print(result)


def find_number_position(numbers, target):
    start_time = time.time()
    for i in range(len(numbers)):
        if numbers[i] == target:
            end_time = time.time()
            print(f"Execution Time: {end_time - start_time:.10f} seconds")
            return i
    return -1  # If the target is not found, return -1 or handle accordingly

numbers = [12, 34, 68, 45, 68, 89]
target_number = 68
result = find_number_position(numbers, target_number)
print(result)