# Stack Data Structure

A **stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle. The last element added to the stack is the first one removed. Think of it as a stack of plates: you add and remove plates from the top.

## Key Concepts

- **LIFO Principle**: Last element pushed is the first to be popped.
- **Top of the Stack**: The most recently added element.
- **Overflow/Underflow**: An overflow occurs when adding to a full stack, and an underflow occurs when removing from an empty stack.

## Types of Stack

1. **Fixed Size Stack**: 
   - Has a predefined capacity.
   - Overflow and underflow conditions can occur.

2. **Dynamic Size Stack**: 
   - Can grow or shrink as needed.
   - Typically implemented using linked lists.

## Basic Operations

| Operation | Description                                         | Time Complexity | Space Complexity |
|-----------|-----------------------------------------------------|-----------------|------------------|
| `push()`  | Adds an element to the top of the stack.           | O(1)            | O(1)             |
| `pop()`   | Removes the top element from the stack.             | O(1)            | O(1)             |
| `top()`   | Returns the top element without removing it.        | O(1)            | O(1)             |
| `isEmpty()`| Checks if the stack is empty.                      | O(1)            | O(1)             |
| `isFull()`| Checks if the stack is full.                       | O(1)            | O(1)             |

## Implementation

Stacks can be implemented in two main ways:

- **Using Arrays**: Simple and memory-efficient, but lacks dynamic resizing.
- **Using Linked Lists**: Allows dynamic sizing, but requires extra memory for pointers.
- [Stack Implementation](https://github.com/henok-getahun/DataStructureAndAlgorithm-DSA-/blob/main/STACK.py)

## Advantages

- **Simplicity**: Easy to understand and implement.
- **Efficiency**: Constant time complexity for basic operations.
- **Memory Usage**: More memory-efficient compared to some other structures.

## Disadvantages

- **Limited Access**: Elements can only be accessed from the top.
- **Overflow Risks**: Can run out of space if not managed.
- **No Random Access**: Not suitable for scenarios requiring random access.

## Applications

- **Function Call Management**: Used to handle function calls in programming languages.
- **Undo Features**: In applications like text editors and graphic software.
- **Expression Evaluation**: Useful in converting infix expressions to postfix or prefix.

---





