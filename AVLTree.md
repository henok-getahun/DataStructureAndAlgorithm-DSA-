                             AVLTREE
#### 1. Definition
An **AVL Tree** (Adelson-Velsky and Landis Tree) is a self-balancing binary search tree (BST) in which the heights of the two child subtrees of any node differ by at most one. This property ensures that the tree remains approximately balanced, allowing for efficient operations.

#### 2. Applications
AVL trees are utilized in various applications due to their balanced structure, which facilitates efficient data retrieval and manipulation. Common applications include:
- **Databases**: For indexing and maintaining sorted data.
- **Memory Management**: Managing free space in memory allocation.
- **Implementing Sets and Maps**: Serving as a data structure for associative arrays.
- **Network Routers**: For maintaining routing tables.

#### 3. Operations Performed
Here are the main operations performed on AVL trees.

**a. Insertion**
1. Start at the root node and compare the value to be inserted with the current node's value.
2. If the value is less than the current node's value, move to the left child; if greater, move to the right child.
3. Repeat this process until an empty position is found (where the child is None).
4. Insert the new node at this empty position.
5. After insertion, update the height of the nodes along the path back to the root.
6. Calculate the balance factor for each node.
7. If the balance factor is greater than 1 or less than -1, perform the appropriate rotation(s) to restore balance:
   - **Left Left Case**: Perform a right rotation.
   - **Left Right Case**: Perform a left rotation followed by a right rotation.
   - **Right Right Case**: Perform a left rotation.
   - **Right Left Case**: Perform a right rotation followed by a left rotation.

**b. Deletion**
1. Start at the root node and compare the value to be deleted with the current node's value.
2. If the value is less, move to the left child; if greater, move to the right child.
3. Continue this process until the node containing the value is found.
4. If the node has no children, simply remove it.
5. If the node has one child, replace it with its child.
6. If the node has two children, find the minimum value node in the right subtree, replace the value of the node to be deleted with this minimum value, and then delete the minimum value node.
7. After deletion, update the height of the nodes along the path back to the root.
8. Calculate the balance factor for each node.
9. If the balance factor is greater than 1 or less than -1, perform the appropriate rotation(s) to restore balance, similar to the insertion process.

**c. Searching**
1. Start at the root node and compare the target value with the current node's value.
2. If the target value matches the current node's value, the search is successful.
3. If the target value is less than the current node's value, move to the left child; if greater, move to the right child.
4. Repeat this process until the target value is found or a None child is reached, indicating that the target is not present in the tree.

**d. Traversals**
- **In-order Traversal**: 
  1. Start at the root node.
  2. Recursively traverse the left subtree.
  3. Visit the current node (process its value).
  4. Recursively traverse the right subtree.
  
- **Pre-order Traversal**: 
  1. Start at the root node.
  2. Visit the current node (process its value).
  3. Recursively traverse the left subtree.
  4. Recursively traverse the right subtree.

- **Post-order Traversal**: 
  1. Start at the root node.
  2. Recursively traverse the left subtree.
  3. Recursively traverse the right subtree.
  4. Visit the current node (process its value).

[CODE IMPLEMENTAION OF AVL TREE](https://github.com/henok-getahun/DataStructureAndAlgorithm-DSA-/blob/main/AVLTree.py)

#### 4. Time and Space Complexity

| Operation      | Time Complexity | Space Complexity |
|----------------|-----------------|------------------|
| Insertion      | O(log n)        | O(1)             |
| Deletion       | O(log n)        | O(1)             |
| Searching      | O(log n)        | O(1)             |
| Traversal      | O(n)            | O(h) (h is height of tree) |

#### 5. Important Concepts
- **Balance Factor**: The balance factor of a node is defined as the height of its left subtree minus the height of its right subtree. For an AVL tree, the balance factor can be -1, 0, or 1.
  
- **Rotations**: To maintain balance during insertions and deletions, AVL trees perform rotations:
  - **Right Rotation**: Used when a left-heavy subtree needs balancing.
  - **Left Rotation**: Used when a right-heavy subtree needs balancing.
  - **Left-Right Rotation**: A combination of left and right rotations.
  - **Right-Left Rotation**: A combination of right and left rotations.

- **Height**: The height of an AVL tree is always O(log n), ensuring efficient operations even in the worst case.

### Conclusion
AVL trees are an essential data structure that provides efficient operations for dynamic sets. Their self-balancing property ensures that operations remain efficient, making them suitable for various applications in computer science.
