# Notes on Recursion

### Introduction to Recursion
**Definition**: Recursion is a process where a function calls itself directly or indirectly. A function that does this is known as a recursive function.

### Properties of Recursion
- Performs operations multiple times with different inputs.
- Breaks problems into smaller subproblems.
- Requires a base condition to avoid infinite loops.

### Types of Recursion

- **Direct Recursion**: Function calls itself.
- **Indirect Recursion**: Function calls another function that eventually calls the first function.

### Tail vs. Non-Tail Recursion

- **Tail Recursion**: The recursive call is the last action in the function.
- **Non-Tail Recursion**: Other operations occur after the recursive call.

### Advantages of Recursion

- Simplifies code for inherently recursive problems.
- Makes complex problems easier to implement and understand.

### Disadvantages of Recursion

- Higher memory usage due to stack frames.
- Increased time complexity due to function call overhead.
- Potential for stack overflow if not managed properly.

### Real Applications of Recursion

- **Tree and Graph Traversal**: Systematic exploration of nodes.
- **Sorting Algorithms**: Quicksort and mergesort.
- **Divide-and-Conquer**: Binary search.
- **Fractal Generation**: Creating complex patterns.
- **Backtracking**: Exploring decision paths.
- **Memoization**: Caching results of expensive function calls.

### Algorithm Steps for Implementing Recursion
1. **Define a Base Case**: Identify the simplest case with a known solution.
2. **Define a Recursive Case**: Break down the problem into smaller versions and call the function recursively.
3. **Ensure Termination**: Make sure the recursive function eventually reaches the base case.
4. **Combine Solutions**: Merge results from subproblems to solve the original problem.

### Mathematical Interpretation
##### Example for summing first `n` natural numbers:

- **Iterative Approach**:  
  `f(n) = 1 + 2 + 3 + ... + n`

- **Recursive Approach**:
  ```text
  f(n) = {
      1            if n = 1
      n + f(n-1)   if n > 1
  }
### Memory Allocation in Recursion

When any function is called from `main()`, memory is allocated to it on the stack.function calls itself, the memory for the called function is allocated on top of the memory allocated to the calling function,
and a different copy of local variables is created for each function call. When the base case is reached, the function returns its value to the function that called it, and memory is deallocated. This process continues until all recursive calls are resolved.

### Recursion vs. Iteration

| SR No. | Recursion                                          | Iteration                                        |
|--------|----------------------------------------------------|--------------------------------------------------|
| 1)     | Terminates when the base case becomes true.       | Terminates when the condition becomes false.    |
| 2)     | Used with functions.                               | Used with loops.                                |
| 3)     | Every recursive call needs extra space in the stack memory. | Every iteration does not require any extra space. |
| 4)     | Smaller code size.                                 | Larger code size.                               |


