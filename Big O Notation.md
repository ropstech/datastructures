# Big O Notation

## General Explanation
Big O Notation is a mathematical notation used to describe the efficiency of an algorithm in terms of its time complexity. Specifically, it indicates how the runtime of an algorithm grows in relation to the size of its input. It serves as a measure of algorithmic efficiency, providing insights into how well an algorithm can handle larger datasets. The notation is expressed using "O" followed by a function that represents the upper bound of the algorithm's growth rate concerning input size.

In verbal communication, "O(n)" is often spoken as "order of n." It represents the upper bound or worst-case scenario for the growth rate of an algorithm in relation to the size of its input.

## Rulues of Big O

- Keep only the fastest growing term
- Drop constants

**Explanation:**

time = 6*n² + 2*n + 20 

b+n + c becomes irrelevant when the value of n is very large.

## Common Big O Notations

**O(1) - Constant Time Complexity:**

- Description: The algorithm's runtime is constant, regardless of the size of the input.
- Example: Accessing an element in an array by index.
```python
def get_first_element(numbers):
    return numbers[0]
```

**O(log n) - Logarithmic Time Complexity:**

- Description: The runtime grows logarithmically as the size of the input increases.
- Example: Binary search in a sorted array.
```python
def binary_search(sorted_list, target):
    # Assumes sorted_list is sorted
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**O(n) - Linear Time Complexity:**

- Description: The runtime grows linearly with the size of the input.
- Example: Iterating through elements in an array.
```python
def sum_elements(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
```

**O(n log n) - Linearithmic Time Complexity:**

- Description: Common in efficient sorting algorithms like merge sort or heap sort.
- Example: Merge sort.
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**O(n^2) - Quadratic Time Complexity:**

- Description: The runtime is proportional to the square of the size of the input.
- Example: Nested loops iterating over the elements of an array.
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

**O(n^c) - Polynomial Time Complexity:**

- Description: The runtime is a polynomial function of the input size.
- Example: Algorithms with nested loops where the number of nested loops is constant.
```python
def nested_loops(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            print(arr[i] * arr[j])
```

**O(2^n) - Exponential Time Complexity:**

- Description: The runtime doubles with each addition to the input size.
- Example: Recursive algorithms without proper optimization.
```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
```

**O(n!) - Factorial Time Complexity:**

- Description: The runtime grows as the factorial of the input size.
- Example: Algorithms with nested loops where the number of nested loops is proportional to the input size.
```python
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
```

## Interview Questions

**Question:** You are given an array of integers. Write a function to find the position of a specific target integer in the array. If the target is not present, return -1.

```python
# Answer:
def find_number_position(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return None

numbers = [12, 34, 68, 45, 68, 89]
target_number = 68
# Execution Time: 0.0000047684 seconds
```

**Additional Question:** The current function (_find_number_position_) has a time complexity of O(n), which is deemed too slow for large datasets. Please modify the function to achieve a more efficient time complexity

```python
def binary_search(numbers, target):
    low, high = 0, len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None
numbers = [12, 34, 68, 45, 68, 89]
target_number = 68
# Execution Time: 0.0000011921 seconds
```

