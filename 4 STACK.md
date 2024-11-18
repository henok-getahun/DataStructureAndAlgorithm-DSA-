
### STACK

#### 1. Definition
A **Stack** is a linear data structure that follows the Last In First Out (LIFO) principle, meaning that the last element added to the stack will be the first one to be removed. This can be visualized as a stack of plates, where you can only add or remove the top plate. 

#### 2. Characteristics
- **LIFO Order**: The most recently added element is the first to be removed.
- **Dynamic Size**: Stacks can grow and shrink as elements are added or removed, especially when implemented using linked lists.
- **Two Main Operations**: The primary operations of a stack are Push (adding an element) and Pop (removing an element).

#### 3. Types of Stacks
Stacks can be implemented in various forms, each serving different needs:

- **Simple Stack**: The basic form of a stack where elements are added and removed from the same end.

- **Dynamic Stack**: A stack that can grow and shrink in size dynamically, typically implemented using linked lists.

- **Array-Based Stack**: A stack implemented using a fixed-size array, which has a maximum capacity.

- **Function Call Stack**: A special case of a stack used by programming languages to manage function calls and local variables.

#### 4. Applications
Stacks are widely used in various computing scenarios due to their efficient handling of ordered data. Common applications include:

- **Function Calls**: Managing function calls in programming languages, where each call is pushed onto the stack, and once it completes, it is popped off.

- **Expression Evaluation**: Evaluating expressions in postfix (Reverse Polish Notation) and infix notation using stacks to hold operators and operands.

- **Backtracking Algorithms**: Used in algorithms that require exploring multiple paths, such as maze solving or the N-Queens problem.

- **Undo Mechanisms**: Implementing undo functionality in applications, where the last action can be reverted by popping the last state off the stack.

- **Syntax Parsing**: Compilers use stacks to parse syntax and manage the order of operations in expressions.

#### 5. Operations Performed
Here are the main operations performed on stacks:

**a. Push**
1. To add an element to the stack, create a new node (or use an array index).
2. If the stack is implemented using an array, check if there is space available; if not, return an error (overflow).
3. If there is space, increment the top index (or pointer) and assign the new value to the stack at this position.

**b. Pop**
1. To remove an element from the stack, check if the stack is empty; if it is, return an error (underflow).
2. If the stack is not empty, retrieve the value at the top index (or pointer).
3. Decrement the top index (or pointer) to remove the element from the stack.

**c. Peek (or Top)**
1. To access the top element of the stack without removing it, check if the stack is empty.
2. If it is not empty, return the value at the top index.

**d. IsEmpty**
1. To check if the stack is empty, verify if the top index is -1 (or if the pointer is None).
2. Return True if the stack is empty; otherwise, return False.

**e. Size**
1. To determine the number of elements in the stack, maintain a count variable that is updated during push and pop operations.
2. Return the count variable when requested.

- [Stack Code Implementation](https://github.com/henok-getahun/DataStructureAndAlgorithm-DSA-/blob/main/4%20STACK.py)

#### 6. Time and Space Complexity

| Operation      | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
|----------------|----------------------------|-------------------------|------------------|
| Push           | O(1)                       | O(1)                    | O(n)             |
| Pop            | O(1)                       | O(1)                    | O(n)             |
| Peek           | O(1)                       | O(1)                    | O(1)             |
| IsEmpty        | O(1)                       | O(1)                    | O(1)             |
| Size           | O(1)                       | O(1)                    | O(1)             |

#### 7. Important Concepts
- **Top**: The pointer or reference to the most recently added element in the stack. It indicates where elements will be popped from.

- **Dynamic vs. Static Implementation**: Stacks can be implemented using arrays (static) or linked lists (dynamic). The choice of implementation affects performance and memory usage.

- **Stack Overflow and Underflow**: Stack overflow occurs when trying to push an element onto a full stack, while stack underflow occurs when trying to pop an element from an empty stack.

- **Memory Management**: Stacks utilize memory efficiently by allowing for dynamic allocation and deallocation of nodes (in linked list implementations).

### Conclusion
Stacks are fundamental data structures that provide an efficient way to manage ordered collections of elements. Their LIFO nature makes them suitable for various applications in computing, from function call management to expression evaluation. Understanding the different types of stacks and their operations is essential for implementing effective algorithms and data processing systems.




