# Data Structures Roadmap

# Table of Contents

1. [Big O Notation](Big%20O%20Notation.md)
    - [General Explanation](Big%20O%20Notation.md#general-explanation)
    - [Rulues of Big O](Big%20O%20Notation.md#rulues-of-big-o)
    - [Common Big O Notations](Big%20O%20Notation.md#common-big-o-notations)
2. [Arrays](#2-arrays)
    - [Static Arrays](#a-static-arrays)
    - [Dynamic Arrays](#b-dynamic-arrays)
    - [Amortized Analysis](#c-amortized-analysis)


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