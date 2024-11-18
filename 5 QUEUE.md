
###  QUEUE

#### 1. Definition
A **Queue** is a linear data structure that follows the First In First Out (FIFO) principle, meaning that the first element added to the queue will be the first one to be removed. A queue is often likened to a line of people waiting for service, where the person who arrives first is served first. 

#### 2. Characteristics
- **FIFO Order**: Elements are added at the rear and removed from the front.
- **Dynamic Size**: Queues can grow and shrink as elements are added or removed, especially when implemented using linked lists.
- **Two Main Operations**: The primary operations of a queue are Enqueue (adding an element) and Dequeue (removing an element).

#### 3. Types of Queues
Queues can be implemented in various forms, each serving different needs:

- **Simple Queue**: The basic form of a queue where elements are added at the rear and removed from the front.
  
- **Circular Queue**: A more efficient version of a simple queue where the last position is connected back to the first position, forming a circle. It helps in utilizing space better and avoids the problem of unused space in a simple queue.

- **Priority Queue**: A specialized queue where each element has a priority assigned to it. Elements are dequeued based on their priority rather than their order in the queue. Higher priority elements are served before lower priority ones.

- **Double-Ended Queue (Deque)**: A queue where elements can be added or removed from both the front and the rear. This allows for more flexible operations compared to standard queues.

#### 4. Applications
Queues are widely used in various computing scenarios due to their efficient handling of ordered data. Common applications include:

- **Task Scheduling**: Operating systems use queues to manage tasks or processes that need to be executed. For instance, print jobs are queued for processing.

- **Breadth-First Search (BFS)**: Queues are utilized in graph algorithms like BFS to keep track of nodes that need to be explored.

- **Buffering**: Queues are used in data buffering, such as in IO operations, where data is temporarily stored before processing.

- **Call Center Systems**: Managing incoming calls where customers are served in the order they arrive.

- **Asynchronous Data Transfer**: Queues are used in scenarios where data is transferred between processes or threads, ensuring orderly processing.

#### 5. Operations Performed
Here are the main operations performed on queues:

**a. Enqueue**
1. To add an element to the queue, create a new node containing the data.
2. If the queue is empty, set both the front and rear pointers to the new node.
3. If the queue is not empty, set the next pointer of the current rear node to point to the new node.
4. Update the rear pointer to the new node.
5. If using a circular queue, ensure that the rear pointer wraps around to the front if it reaches the end of the array.

**b. Dequeue**
1. To remove an element from the queue, check if the queue is empty; if it is, return an error or indication that the queue is empty.
2. Retrieve the data from the front node.
3. Update the front pointer to point to the next node in the queue.
4. If the queue becomes empty after this operation, reset both the front and rear pointers to None.
5. If using a circular queue, update the front pointer to wrap around appropriately.

**c. Peek (or Front)**
1. To access the front element of the queue without removing it, check if the queue is empty.
2. If it is not empty, return the data from the front node.

**d. IsEmpty**
1. To check if the queue is empty, simply verify if the front pointer is None.
2. Return True if the front is None; otherwise, return False.

**e. Size**
1. To determine the number of elements in the queue, maintain a count variable that is updated during enqueue and dequeue operations.
2. Return the count variable when requested.

- [Queue Code Implementation](https://github.com/henok-getahun/DataStructureAndAlgorithm-DSA-/blob/main/5%20QUEUE.py)
#### 6. Time and Space Complexity

| Operation      | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
|----------------|----------------------------|-------------------------|------------------|
| Enqueue        | O(1)                       | O(1)                    | O(1)             |
| Dequeue        | O(1)                       | O(1)                    | O(1)             |
| Peek           | O(1)                       | O(1)                    | O(1)             |
| IsEmpty        | O(1)                       | O(1)                    | O(1)             |
| Size           | O(1)                       | O(1)                    | O(1)             |

#### 7. Important Concepts
- **Front**: The pointer or reference to the first element in the queue. It indicates where elements will be dequeued from.

- **Rear**: The pointer or reference to the last element in the queue. It indicates where new elements will be enqueued.

- **Circular Nature**: In a circular queue, the last position connects back to the first position, allowing for efficient use of space and reducing the chances of overflow.

- **Dynamic vs. Static Implementation**: Queues can be implemented using arrays (static) or linked lists (dynamic). The choice of implementation affects performance and memory usage.

### Conclusion
Queues are fundamental data structures that provide an efficient way to manage ordered collections of elements. Their FIFO nature makes them suitable for various applications in computing, from task scheduling to data buffering. Understanding the different types of queues and their operations is essential for implementing effective algorithms and data processing systems.
