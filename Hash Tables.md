# Hash Tables:


- [General Explanation](#general-explanation)
    - [Key Features](#key-featuures)
- [Common Big O Notations](#common-big-o-notations)
- [Python Implementation](#python-implementation)
- [Interview Questions](#interview-questions)


## General Explanation
Hash tables, also known as hash maps or dictionaries in Python, are data structures that store key-value pairs. They use a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

### Key Features:
- Fast Lookup: Hash tables provide constant-time average-case performance for key-based operations such as lookup, insertion, and deletion.
- Key-Value Pair Storage: Each element in a hash table consists of a key-value pair, where the key is unique.
- Dynamic Size: Hash tables can dynamically resize themselves to accommodate more key-value pairs as needed, without requiring pre-allocation of memory.

</br>**Advantages:**
</br>Fast Access: Hash tables offer constant-time average-case lookup, insertion, and deletion operations, making them highly efficient for storing and retrieving data.
</br>Flexible Key Types: In Python, hash tables (dictionaries) allow keys of various types, including strings, integers, tuples, and more.
</br>Versatile Usage: Hash tables are widely used in various applications, such as databases, caching mechanisms, symbol tables, and more, due to their fast lookup times and flexibility.

**Disadvantages:**
</br>Space Complexity: Hash tables may consume more memory than other data structures, especially when the load factor (ratio of occupied slots to total slots) is high.
</br>Hash Function Dependency: The performance of a hash table depends heavily on the quality of the hash function used. A poor hash function can lead to collisions, resulting in degraded performance.
</br>Iteration Order: The order of elements in a hash table is not guaranteed to be consistent across iterations, which can be problematic in certain scenarios where order matters.

## Common Big O Notations
- Lookup (Average Case): O(1)
- Insertion (Average Case): O(1)
- Deletion (Average Case): O(1)


## Python Implementation:
In Python, hash tables are implemented using dictionaries (dict). Below is an example of using a hash table to store and retrieve key-value pairs:

```python
from typing import Dict, Any

# Define a hash table using a dictionary
HashTable = Dict[str, Any]


def create_hash_table() -> HashTable:
    """Create an empty hash table."""
    return {}


def insert_into_hash_table(hash_table: HashTable, key: str, value: Any) -> None:
    """Insert a key-value pair into the hash table."""
    hash_table[key] = value


def lookup_in_hash_table(hash_table: HashTable, key: str) -> Any:
    """Lookup the value associated with the given key in the hash table."""
    return hash_table.get(key)


def main():
    # Create an empty hash table
    hash_table = create_hash_table()

    # Insert key-value pairs
    insert_into_hash_table(hash_table, 'name', 'John')
    insert_into_hash_table(hash_table, 'age', 30)

    # Lookup values by keys
    name = lookup_in_hash_table(hash_table, 'name')
    age = lookup_in_hash_table(hash_table, 'age')

    # Print the retrieved values
    print(f"Name: {name}")  # Output: Name: John
    print(f"Age: {age}")    # Output: Age: 30


if __name__ == "__main__":
    main()

```