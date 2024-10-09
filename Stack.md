# Stack Data Structure

A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle. It operates such that the last element added is the first one removed.

## Key Concepts
- The **top** of the stack is the reference to the last added element.
- Stacks can be implemented using either arrays or linked lists.

## Types of Stack
1. **Fixed Size Stack**: Has a fixed capacity and cannot grow or shrink dynamically.
2. **Dynamic Size Stack**: Can dynamically grow or shrink as required.

## Basic Operations
- `push()`: Inserts an element onto the stack.
- `pop()`: Removes the top element from the stack.
- `top()`: Returns the top element without removing it.
- `isEmpty()`: Returns `true` if the stack is empty, otherwise `false`.
- `isFull()`: Returns `true` if the stack is full, otherwise `false`.

## Stack Implementation
Stacks can be implemented in two main ways:
1. **Using an Array**
2. **Using a Linked List**

[Stack Implementation on HackerRank](https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true)

## Advantages
- **Simplicity**: Stacks are easy to implement and understand.
- **Efficiency**: `push` and `pop` operations run in constant time `O(1)`.
- **LIFO Principle**: Stacks naturally follow the LIFO principle, making them suitable for tasks like function call management and expression evaluation.
- **Memory Efficiency**: Stacks only need to store active elements, making them space-efficient.

## Disadvantages
- **Limited Access**: Only the top element is directly accessible.
- **Overflow Risk**: A fixed-size stack may overflow if capacity is exceeded.
- **No Random Access**: Stacks do not allow for direct access to elements in the middle.
- **Limited Capacity**: Fixed-size stacks have a predefined limit, which may be insufficient in some cases.

## Applications
- **Infix to Postfix/Prefix conversions**
- **Undo/Redo functionality** in text editors and graphic design software.
- **Forward/Backward navigation** in web browsers.
- **Memory Management** in modern operating systems.
- **Function Call Management**: Managing recursive function calls or nested function calls in programming.

---

Feel free to copy and paste this markdown directly into your `README.md` file on GitHub! The content is structured for easy readability and clarity.
