# Linked Lists

- [General Explanation](#general-explanation)
    - [Double Linked Lists](#double-linked-lists)
- [Common Big O Notations](#common-big-o-notations)
    - [Comparison of Arrays and Linked Lists](#comparison-of-arrays-and-linked-lists)
- [Python Implementation](#python-implementation)
- [Interview Questions](#interview-questions)

## General Explanation
A linked list is a data structure consisting of nodes where each node points to the next node in the sequence. Unlike arrays, linked lists do not have a fixed size, and their elements are not stored in contiguous memory locations.

<img src=https://media.geeksforgeeks.org/wp-content/uploads/20220712172013/Singlelinkedlist.png alt="Linked Liist Exaplanation Image">


### Two Main Benefits Over an Array
**You don't need to preallocate space.**
<br/> -> Linked lists operate differently. When you add a new element to a linked list, memory is dynamically allocated for that specific element. Each element (node) in the linked list contains a reference to the next node, allowing the list to dynamically grow or shrink during runtime.

- **Benefits of Dynamic Allocation in Linked Lists:**
    1. **Dynamic Size:** 
    <br/>Linked lists can easily accommodate a variable number of elements without requiring preallocation. You can keep adding elements, and memory is allocated on-the-fly.

    2. **No Wasted Memory:** 
    <br/>Memory is used efficiently. If you have a linked list with only three elements, it only uses memory for those three elements, not more.

    3. **Flexibility:** 
    <br/>Linked lists provide flexibility in managing memory. They allow for efficient memory utilization, especially when the size of the data structure is unpredictable.

**Insertion is easiert**


### Double Linked Lists
Here you not only have a reference to the next element, but also to the previous element.

<img src=https://www.boardinfinity.com/blog/content/images/2022/11/Untitled-design--16-.jpg alt="Double Linked List Explanation Image">

## Common Big O Notations

- Insert Element at the beginning -> **_O(1)_**
- Delete Element at the beginning -> **_O(1)_**
- Insert/Delete Element at the end or in the middle -> **_O(n)_** because you have to iterate through the elements

### Comparison of Arrays and Linked Lists
| |  Array | Linked List | 
|---|---|---:|
| Indexing  | O(1)  | O(n) |
| Insert/Delete Element at Start  | O(n) | O(1) |
| Insert/Delete Element at End  | O(1)  | O(n)  |
| Insert Element in the Middle  | O(n)  | O(n)  |

## Python Implementation

```python
from typing import Iterable

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        return

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        iterator = self.head
        while iterator.next:
            iterator = iterator.next

        iterator.next = Node(data, None)

    def insert_values(self, data_list: Iterable):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next
        
        return count

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        iterator = self.head
        while iterator:
            if count == index -1:
                iterator.next = iterator.next.next
                break

            iterator = iterator.next
            count += 1
    
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        iterator = self.head
        while iterator:
            if count == index -1:
                node = Node(data, iterator.next)
                iterator.next = node
                break

            iterator = iterator.next
            count += 1

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        iterator = self.head
        llstr = ''

        while iterator:
            llstr += str(iterator.data) + '-->'
            iterator = iterator.next

        print(llstr)



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(9)
    ll.insert_values([2, 76, 92, 14, 65])
    ll.insert_at(0, 666)
    ll.print()

# -> 666-->2-->76-->92-->14-->65-->
```
