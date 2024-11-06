### Linked Lists

#### 1. Definition
A **Linked List** is a linear data structure in which elements, called nodes, are stored in a sequence. Each node contains two components: data and a reference (or pointer) to the next node in the sequence. Unlike arrays, linked lists do not require contiguous memory allocation, allowing for dynamic memory usage and efficient insertions and deletions.

#### 2. Types of Linked Lists
- **Singly Linked List**: Each node contains data and a pointer to the next node. The last node points to None.
- **Doubly Linked List**: Each node contains data, a pointer to the next node, and a pointer to the previous node, allowing traversal in both directions.
- **Circular Linked List**: The last node points back to the first node, forming a circle. This can be singly or doubly linked.

#### 3. Applications
Linked lists are widely used in various applications due to their dynamic nature. Common applications include:
- **Dynamic Memory Allocation**: Managing memory more efficiently than static arrays.
- **Implementing Stacks and Queues**: Using linked lists to create these abstract data types.
- **Adjacency Lists**: Representing graphs.
- **Undo Functionality in Applications**: Storing previous states or actions.
- **Sparse Matrices**: Efficiently representing matrices with many zero values.

#### 4. Operations Performed
Here are the main operations performed on linked lists.

**a. Insertion**
1. To insert a new node, create the node and set its data.
2. If inserting at the beginning, set the new node’s next pointer to the current head and update the head to the new node.
3. If inserting at the end, traverse the list to find the last node, set its next pointer to the new node, and set the new node’s next pointer to None.
4. If inserting at a specific position, traverse the list to the desired position, adjust the pointers of the surrounding nodes to include the new node.

**b. Deletion**
1. To delete a node, start at the head and traverse the list to find the node to be deleted.
2. If the node to be deleted is the head, update the head to the next node.
3. If the node is in the middle or at the end, adjust the next pointer of the previous node to skip the node being deleted.
4. If the node is not found, indicate that the deletion was unsuccessful.

**c. Searching**
1. Start at the head node and compare the target value with the current node's data.
2. If the target value matches, the search is successful.
3. If not, move to the next node and repeat the comparison until the target is found or the end of the list is reached.

**d. Traversals**
- **Forward Traversal**: Start at the head node and traverse through the list by following the next pointers until reaching the end (None).
  
- **Backward Traversal**: (Applicable only in doubly linked lists) Start at the tail node and traverse backward using the previous pointers until reaching the head.
- [Linked List Code Implmentation](https://github.com/henok-getahun/DataStructureAndAlgorithm-DSA-/blob/main/Linked%20List.py)
#### 5. Time and Space Complexity

| Operation      | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
|----------------|----------------------------|-------------------------|------------------|
| Insertion      | O(1) (at head) or O(n) (at end or specific position) | O(n)                    | O(1)             |
| Deletion       | O(1) (at head) or O(n) (specific node) | O(n)                    | O(1)             |
| Searching      | O(n)                       | O(n)                    | O(1)             |
| Traversal      | O(n)                       | O(n)                    | O(1)             |

#### 6. Important Concepts
- **Head**: The first node in the linked list. It is a reference point for accessing the list.
  
- **Tail**: The last node in the linked list, which points to None (or the first node in a circular linked list).

- **Memory Allocation**: Linked lists allocate memory dynamically, allowing for flexible data structure sizing.

### Conclusion
Linked lists are a fundamental data structure that provides a flexible way to store and manage collections of data. Their ability to efficiently handle dynamic memory allocation makes them suitable for various applications, though they may incur higher memory overhead compared to arrays due to pointer storage.




