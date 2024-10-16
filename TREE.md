# Binary Tree Overview

## What is a Binary Tree?
A binary tree is a data structure composed of nodes, where each node has at most two children referred to as:
- **Left Child**
- **Right Child**

Binary trees are used to represent hierarchical data and provide efficient operations like searching, insertion, and deletion compared to linear structures such as arrays or linked lists. They are widely used in various algorithms and data structures, including:
- Binary Search Trees (BST)
- Heaps
- Expression Trees

### Importance of Binary Trees
- They lay the foundation for more advanced data structures.
- They provide efficient solutions for a wide range of computational problems, especially where relationships between elements must be maintained.

## Terminologies in Binary Tree
- **Root**: The topmost node in the tree. There is only one root in a binary tree.
- **Node**: Each individual element in the tree, consisting of a value, left child, and right child.
- **Child**: The nodes below the current node.
- **Parent**: The node above the current node.
- **Leaf**: A node that has no children, i.e., both its left and right references are `None`.
- **Internal Node**: A node that has at least one child.
- **Subtree**: A tree formed by a node and its descendants.
- **Depth**: The number of edges from the root to a specific node.
- **Height**: The number of edges from a specific node to the farthest leaf.
- **Level**: The level of a node is determined by the number of edges from the root to the node. The root is at level 0.

## Properties of Binary Tree
- The maximum number of nodes at level \( l \) is \( 2^l \).
  - For example, at level 0, there is 1 node; at level 1, there are 2 nodes; and so on.
- The maximum number of nodes in a binary tree of height \( h \) is \( 2^{(h+1)} - 1 \).
- A binary tree with \( n \) nodes has \( n - 1 \) edges.
- The height of a balanced binary tree is \( O(\log n) \), where \( n \) is the number of nodes.

## Representation of Binary Tree

### Linked Node Representation
Each node of a binary tree is represented as an object with three main parts:
- **Data**: Holds the value stored in the node.
- **Left Child**: A reference (pointer) to the left child node.
- **Right Child**: A reference (pointer) to the right child node.

### Array Representation
Binary trees can also be represented using arrays, where the parent-child relationships are defined by the index:
- For any node at index \( i \):
  - The left child is at index \( 2i + 1 \)
  - The right child is at index \( 2i + 2 \)
- The root node is located at index 0.

### Example

        1
       / \
      2   3
     / \
    4   5

# Types of Binary Tree

- **Full Binary Tree**: Every node has either 0 or 2 children. No node has exactly one child.
  
  **Example:**
  ```plaintext
      1
     / \
    2   3
   / \
  4   5

# Complete Binary Tree

1 **Complete Binary Tree** is a type of binary tree in which all levels are fully filled except possibly for the last level, which is filled from left to right.

## Example
```plaintext
    1
   / \
  2   3
 / \
4   5
```
# Perfect Binary Tree

2 **Perfect Binary Tree** is a binary tree in which all internal nodes have exactly two children, and all leaf nodes are at the same level.

## Example
```plaintext
     1
    / \
   2   3
  / \ / \
 4  5 6  7
```
# Balanced Binary Tree

3 **Balanced Binary Tree** is a tree where the height difference between the left and right subtrees of every node is at most one. Common examples include AVL trees and Red-Black trees.

## Example
```plaintext
    1
   / \
  2   3
```
# Degenerate (Skewed) Tree

4 **Degenerate (Skewed) Tree** is a tree where each parent node has only one child. This can either be a left-skewed tree or a right-skewed tree.

## Example
```plaintext
    1
     \
      2
       \
        3
```
# Operations on Binary Tree

## Basic Operations
- **Traversal**: The process of visiting each node in a tree exactly once in a specific order.
- **Insertion**: Adding a new node to the tree while maintaining its properties.
- **Searching**: Finding a node with a specific value in the tree.
- **Deletion**: Removing a node and restructuring the tree to maintain its properties.

## Traversal in Binary Tree
Traversal can be done in several ways:

- **In-order Traversal (Left, Root, Right)**:
  - Visit the left subtree, then the root, and finally the right subtree.
  - Useful for retrieving data in sorted order in binary search trees (BSTs).

- **Pre-order Traversal (Root, Left, Right)**:
  - Visit the root first, then the left subtree, and finally the right subtree.
  - Commonly used for creating a copy of the tree.

- **Post-order Traversal (Left, Right, Root)**:
  - Visit the left subtree, then the right subtree, and finally the root.
  - Useful in deleting or freeing the nodes in a tree.

- **Level-order Traversal**:
  - Visit nodes level by level from top to bottom.
  - Also called Breadth-First Search (BFS).
# Operations on Binary Tree

## Insertion in Binary Tree
Insertion into a binary tree typically follows a level-order strategy. The first available position from left to right is filled by the new node to maintain the structure.

### Example (Level-order insertion):
- Start at the root and traverse level by level.
- Insert the new node at the first available spot.

## Searching in Binary Tree
Searching in a binary tree involves traversing the tree and checking each node to see if it contains the target value. It can be done using any traversal method (in-order, pre-order, post-order, level-order).

- **Time Complexity**: In the worst case, searching takes O(n) time in an unbalanced tree, where n is the number of nodes.

## Deletion in Binary Tree
Deletion involves removing a node and restructuring the tree to maintain its properties:
- **Leaf Node Deletion**: The node is removed without further action.
- **Node with One Child**: The node is replaced with its child.
- **Node with Two Children**: Replace the node with the rightmost node in the left subtree (in-order predecessor) or the leftmost node in the right subtree (in-order successor).

## Auxiliary Operations on Binary Tree
- **Height Calculation**: Determines the maximum depth of the tree. It is useful to understand how balanced the tree is.
- **Node Counting**: Count the total number of nodes in the tree.
- **Leaf Counting**: Count the number of leaf nodes (nodes without children).
- **Mirror Image**: Creates a mirror image of the tree by swapping the left and right children of each node.

## Complexity Analysis of Binary Tree Operations
- **Traversal**: O(n), where n is the number of nodes.
- **Insertion**: O(n) in an unbalanced tree, O(log n) in a balanced tree.
- **Searching**: O(n) in the worst case.
- **Deletion**: O(n) in the worst case, especially if the tree is unbalanced.

## Advantages of Binary Tree
- **Efficiency**: Operations like searching, insertion, and deletion are efficient when the tree is balanced, with a time complexity of O(log n).
- **Flexibility**: Binary trees can be adapted to various use cases (e.g., BST, AVL, heaps).
- **Hierarchical Representation**: Represents hierarchical data more naturally compared to other data structures.

## Disadvantages of Binary Tree
- **Unbalanced Trees**: If the tree becomes unbalanced, the time complexity of operations can degrade to O(n).
- **Space Complexity**: Binary trees require more memory due to pointers (for left and right children).

## Applications of Binary Tree
- **Binary Search Trees (BST)**: Efficient for searching, insertion, and deletion.
- **Heaps**: Used for implementing priority queues, sorting algorithms like heap sort.
- **Expression Trees**: Used in compilers to represent and evaluate expressions.
- **Tries**: A specialized form of binary tree used for searching words in a dictionary or implementing autocomplete.
- **Huffman Coding Trees**: Used in data compression algorithms.

