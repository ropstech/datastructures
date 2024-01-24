# Arrays

- [General Information](#general-information)
    - [Comparison of Static and Dynamic Arrays](#comparison-of-static-and-dynamic-arrays)
- [Common Big O Notations](#common-big-o-notations)
    - [1. Lookup by index](#1-lookup-by-index)
    - [2. Lookup by value](#2-lookup-by-value)
    - [3. Array traversal](#3-array-traversal)
    - [4. Array insertion](#4-array-insertion)
    - [5. Array deletion](#5-array-deletion)
- [Interview Questions](#interview-questions)


## General Information

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

### Comparison of Static and Dynamic Arrays
| Feature	Dynamic Arrays  | Static Arrays	  | Dynamic Arrays   | 
|---|---|---|
| Size  |  Fixed | Can grow or shrink  |
| Efficiency  |  Less efficient for operations such as slicing and indexing	 | More efficient for operations such as slicing and indexing  |
| Ease of Use  |  Easier to use | More complex to use  |
| Flexibility  |  Less flexible | More flexible  |



## Common Big 0 Notataions
Underlying example array:

```python
stock_prices = [267, 245, 237, 231, 292]

stock_prices[0] <- 267 <- price on day 1
stock_prices[3] <- 231 <- price on day 4
```


### 1. Lookup by index

```python
# What is the price on day 4 ?
stock_prices[3] -> 231 
```
**O(1) - Constant Time Complexity:**


### 2. Lookup by value

```python
# On what day was the price 245 ?
for i in range(len(stock_prices)):
    if stock_prices[i] == 245:
        return i
```
**O(n) - Linear Time Complexity:**


### 3. Array traversal

```python
# Print all prices
for price in stock_prices:
    print(price)
```
**O(n) - Linear Time Complexity:**


### 4. Array insertion

```python
# Insert new price (254) at index 1
stock_prices.insert(1, 254)
-> [267, 254, 245, 237, 231, 292]
# this will shift all elements after index 1 by one position
```
**O(n) - Linear Time Complexity:**


### 5. Array deletion

```python
# Delete element at index 2
stock_prices.remove(1)
-> [267, 245, 237, 231, 292]
# this will shift all elements after index 1 by one position
```
**O(n) - Linear Time Complexity:**



## Interview Questions