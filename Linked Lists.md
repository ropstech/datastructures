# Linked Lists

- [General Explanation](#general-explanation)
    - [Double Linked Lists](#double-linked-lists)
- [Common Big O Notations](#common-big-o-notations)
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