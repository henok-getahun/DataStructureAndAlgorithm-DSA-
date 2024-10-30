                 BINARY HEAP
1. **Definition**
   
   A Binary Heap is a complete binary tree that satisfies the heap property. In a Max Heap, for any given node, the value of the node is greater than or equal to the values of its children. In a Min Heap, the value of the node is less than or equal to the values of its children. This structure allows for efficient retrieval of the maximum or minimum element.

2. **Applications**
   
   Binary Heaps are widely used in various applications due to their efficient properties for priority management and sorting. Common applications include:
   
   - **Priority Queues**: Binary heaps are often implemented to manage priority queues, allowing for efficient insertion and extraction of the highest (or lowest) priority elements.
   - **Heap Sort**: A comparison-based sorting algorithm that uses the heap data structure to sort elements efficiently in O(n log n) time.
   - **Graph Algorithms**: Used in algorithms like Dijkstra’s and Prim’s for efficiently selecting the next vertex to process.
   - **Memory Management**: Managing free memory blocks in dynamic memory allocation.

3. **Operations Performed**
   
   Here are the main operations performed on Binary Heaps:

   a. **Insertion**
   
   - Start by adding the new element at the end of the heap (the next available position).
   - Compare the added element with its parent; if it violates the heap property (i.e., in a Max Heap, if the new element is greater than its parent), swap them.
   - Continue this process (known as "bubbling up") until the heap property is restored or the element becomes the root.

   b. **Deletion (Extracting the Root)**
   
   - Remove the root element (the maximum for Max Heap or minimum for Min Heap).
   - Replace the root with the last element in the heap.
   - Compare the new root with its children; if it violates the heap property, swap it with the larger (or smaller) child.
   - Continue this process (known as "bubbling down") until the heap property is restored.

   c. **Peeking**
   
   - To retrieve the maximum (or minimum) element without removing it, simply return the root of the heap.

   d. **Heapify**
   
   - This operation converts an arbitrary array into a heap structure. It can be done in-place using a bottom-up approach, ensuring that the heap property is maintained.

   - [binary heap code implementaion](https://github.com/henok-getahun/DataStructureAndAlgorithm-DSA-/blob/main/BinaryHeap.py)

4. **Time and Space Complexity**
   
   | Operation          | Time Complexity | Space Complexity |
   |--------------------|----------------|------------------|
   | Insertion           | O(log n)       | O(1)             |
   | Deletion            | O(log n)       | O(1)             |
   | Peeking             | O(1)           | O(1)             |
   | Heapify            | O(n)           | O(1)             |
   | Traversal          | O(n)           | O(h) (h is height of heap) |

5. **Important Concepts**
   
   - **Heap Property**: The key property that defines a binary heap—Max Heap or Min Heap.
   
   - **Complete Binary Tree**: A binary tree in which all levels are fully filled except possibly for the last level, which is filled from left to right.
   
   - **Bubbling Up and Bubbling Down**: Techniques used to maintain the heap property during insertion and deletion operations.
   

---

### Conclusion

Binary Heaps are fundamental data structures that provide efficient management of priority elements. Their properties and operations make them suitable for a variety of applications in computer science, particularly in algorithms and data management systems.
