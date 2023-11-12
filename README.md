# Data Structures Roadmap

# Table of Contents

[Big O Notation](Big%20O%20Notation.md)

1. [Big O Notation](#1-big-o-notation)
    - [General Explanation](#general-explanation)
    - [Rulues of Big O](#rulues-of-Big-O)
    - [Common Big O Notations](#common-big-o-notations)
2. [Arrays](#2-arrays)
    - [Static Arrays](#a-static-arrays)
    - [Dynamic Arrays](#b-dynamic-arrays)
    - [Amortized Analysis](#c-amortized-analysis)

## 1. Big O Notation

### General Explanation
Big O Notation is a mathematical notation used to describe the efficiency of an algorithm in terms of its time complexity. Specifically, it indicates how the runtime of an algorithm grows in relation to the size of its input. It serves as a measure of algorithmic efficiency, providing insights into how well an algorithm can handle larger datasets. The notation is expressed using "O" followed by a function that represents the upper bound of the algorithm's growth rate concerning input size.

In verbal communication, "O(n)" is often spoken as "order of n." It represents the upper bound or worst-case scenario for the growth rate of an algorithm in relation to the size of its input.

### Rulues of Big O

- Keep only the fastest growing term
- Drop constants

**Explanation:**

time = 6*n² + 2*n + 20 

b+n + c becomes irrelevant when the value of n is very large.

### Common Big O Notations

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


## 2. Arrays

### A. Static Arrays

Arrays are fundamental data structures that store elements of the same data type in contiguous memory locations. Key characteristics of static arrays include:

- **Fixed Size:** Once declared, the size cannot be changed during runtime.
- **Random Access:** Elements can be accessed in constant time using indices.

**Example in Python:**
```python
static_array = [1, 2, 3, 4, 5]
print(static_array[2])  # Output: 3
```

### B. Dynamic Arrays

Dynamic arrays overcome the limitation of fixed size. They automatically resize when the number of elements exceeds the current capacity. In dynamic arrays:

- **Variable Size:** The size can be changed dynamically.
Amortized Constant Time for **Appends:** On average, the time complexity for appending an element is constant.

**Example in Python:**
```python
import array
dynamic_array = array.array('i', [1, 2, 3, 4, 5])

# Appending an element (Amortized O(1))
dynamic_array.append(6)

# Resizing happens behind the scenes if needed
```

### C. Amortized Analysis

Amortized analysis evaluates the time complexity of an algorithm over a sequence of operations. In dynamic arrays, amortized analysis tells us that resizing, even though occasionally taking O(n) time, averages to O(1) per append operation.

Explanation:

- If resizing takes O(n) time, after n append operations, O(n) time is spent on resizing.
- On average, each append operation takes O(1) time.
Example in Python:

**Example in Python:**
```python
# Amortized O(1) append operations
for i in range(10**6):
    dynamic_array.append(i)
```

In summary, dynamic arrays offer resizable arrays with efficient append operations, and amortized analysis provides a realistic view of average operation costs over time.