# Queue Data Structure

A **queue** is a linear data structure that follows the **First In, First Out (FIFO)** rule. Like a line at a counter, the first item added is the first one removed.

## Types of Queues:
1. **Simple Queue**: Basic FIFO queue.
2. **Double-ended Queue (Deque)**: Add and remove elements from both ends.
3. **Circular Queue**: The last position wraps around to the first.
4. **Priority Queue**: Serve elements based on priority.

## Implementation

Queue can be implemented in two main ways:

- **Using Arrays**: Simple and memory-efficient, but lacks dynamic resizing.
- **Using Linked Lists**: Allows dynamic sizing, but requires extra memory for pointers.
- [Queue Implementation](https://github.com/henok-getahun/DataStructureAndAlgorithm-DSA-/blob/main/QUEUE.py)

## Basic Operations and Complexities:
| Operation   | Time Complexity | Space Complexity |
|-------------|-----------------|------------------|
| **Enqueue** | O(1)            | O(1)             |
| **Dequeue** | O(1)            | O(1)             |
| **Peek/Front** | O(1)         | O(1)             |
| **Rear**    | O(1)            | O(1)             |
| **isFull**  | O(1)            | O(1)             |
| **isEmpty** | O(1)            | O(1)             |

## Applications:
- **Task Scheduling**: CPU scheduling, printer spooling.
- **Networking**: Router queues, mail queues.
- **Algorithms**: Breadth-First Search, Topological Sort.

## Advantages:
- Efficient for managing large data sets.
- Easy insertion and deletion.

## Disadvantages:
- Deletion from the middle is slow.
- Searching takes linear time (`O(n)`).

## Key Notes on Queue Data Structure
- **Priority Queue Implementation**: Can be implemented using linked lists, arrays, binary search trees, and heaps (best with heaps).
- **Double-ended Queue (Deque)**: Allows insertion and removal of elements from both ends.
- **Stack vs. Queue**: Use a queue for first-in, first-out (FIFO) order. Use a stack if you want to reverse the order of elements (Last-in, First-out - LIFO).
- **Queue Principle**: Follows FIFO; the first element added is the first to be removed.
- **Types of Queues**: Simple Queue, Double-ended Queue (Deque), Circular Queue, and Priority Queue.
- **Real-life Applications**: Cashier lines, CPU scheduling, disk scheduling, serving requests on shared resources like printers.
- **Limitations**: Middle element deletion isn't possible without first removing preceding elements. Random access takes linear time (`O(n)`).
- **Queue Implementations**: Can be implemented using Arrays or Linked Lists. Array-based queues require a fixed size at declaration.
- **Common Operations**: Enqueue, Dequeue, Peek (Front), Rear, isFull, isEmpty.

---

Queue structures are useful when items need to be processed in order, especially in shared resource scenarios or scheduling tasks.
