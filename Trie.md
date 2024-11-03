
## TRIE
### Definition

A **Trie** (pronounced "try"), also known as a prefix tree or digital tree, is a specialized tree-like data structure that is used to store a dynamic set of strings, where the keys are usually strings. Each node in a Trie represents a single character of a string, and paths from the root to the leaf nodes represent words. Tries are particularly useful for tasks involving prefix matching and retrieval.

### Properties

- **Node Structure**: Each node contains:
  - A dictionary (or array) of children nodes.
  - A boolean flag indicating whether the node represents the end of a word.
  
- **Root Node**: The Trie has a root node that does not contain any character.

- **Complete Words**: A word is considered complete when you reach a node marked as the end of a word.

### Applications

Tries are widely used in various applications due to their efficient properties for string management and retrieval. Common applications include:

- **Autocomplete Systems**: Used in search engines and text editors to suggest completions based on the prefix of the input.
  
- **Spell Checkers**: Efficiently checking the existence of words and suggesting corrections.
  
- **IP Routing**: Storing routing prefixes in networking applications.
  
- **Data Compression**: Implemented in algorithms like LZ77 and LZW for efficient data encoding.

- **Longest Common Prefix**: Finding the longest common prefix among a set of strings.

### Operations Performed

Here are the main operations performed on Tries:

#### a. Insertion

1. Start from the root node.
2. For each character in the word:
   - If the character is not present in the current node’s children, create a new TrieNode.
   - Move to the child node corresponding to the character.
3. After inserting all characters, mark the last node as the end of the word.



#### b. Search

1. Start from the root node.
2. For each character in the word:
   - If the character is not found in the current node’s children, return `False`.
   - Move to the child node corresponding to the character.
3. After processing all characters, return the value of the end_of_word flag of the last node.


#### c. Deletion

1. Start from the root node and traverse to the last character of the word.
2. If the word does not exist, raise an error.
3. Mark the end_of_word flag as `False` for the last character.
4. If the node has no children, remove it by traversing back up the Trie and deleting nodes that are no longer needed.



#### d. Prefix Search

- To find if any words in the Trie start with a given prefix, follow the same procedure as in the search operation, but do not check the end_of_word flag for the last character.

  -  [code implementaion ](https://github.com/henok-getahun/DataStructureAndAlgorithm-DSA-/blob/main/Trie.py)


### Time and Space Complexity

| Operation         | Time Complexity | Space Complexity |
|-------------------|-----------------|------------------|
| Insertion         | O(m)            | O(m)             |
| Search            | O(m)            | O(1)             |
| Deletion          | O(m)            | O(1)             |
| Prefix Search     | O(m)            | O(1)             |
| Traversal         | O(n)            | O(h) (h is height of Trie) |

- **m**: Length of the word being inserted, searched, or deleted.
- **n**: Total number of words in the Trie.
- **h**: Height of the Trie, which is determined by the length of the longest word.

### Important Concepts

- **Trie Structure**: A tree structure where each node represents a character of the string.
- **Prefix**: A substring that is at the start of a string; Tries excel at handling prefixes.
- **End of Word Flag**: A boolean flag that indicates whether a node marks the end of a valid word.

### Conclusion

Tries are powerful data structures that provide efficient management of strings, particularly for applications involving prefix searches, autocomplete features, and dictionary implementations. Their ability to handle dynamic sets of strings makes them suitable for a variety of applications in computer science, particularly in algorithms and data management systems.


