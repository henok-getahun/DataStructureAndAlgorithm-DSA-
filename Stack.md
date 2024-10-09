                                                                          ### Stack




                                                       - is a linear data structure that follows Last In First Out Principle.              
                                                       - To implement the stack, it is required to maintain the pointer to the top of the stack.
                                                       - Types of Stack Data Structure:
                                                                      1, Fixed Size Stack :It has a fixed size and cannot grow or shrink dynamically.
                                                                      2, Dynamic Size Stack : A dynamic size stack can grow or shrink dynamically. 
                                                       #### Basic Operations on Stack Data Structure:  In order to make manipulations in a stack, there are certain operations provided to us
                                                                      1, push() to insert an element into the stack
                                                                      2, pop() to remove an element from the stack
                                                                      3, top() Returns the top element of the stack.
                                                                      4, isEmpty() returns true if stack is empty else false.
                                                                      5, isFull() returns true if the stack is full else false.
                                                       #### Implementation of Stack Data Structure: There are two ways to implement a stack
                                                                      1, Using Array
                                                                      2, Using Linked List
                                       - [Stack Implementation](https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true)
                                                       -Advantages of Stack Data Structure:
           Simplicity: Stacks are a simple and easy-to-understand data structure, making them suitable for a wide range of applications.
            Efficiency: Push and pop operations on a stack can be performed in constant time (O(1)) , providing efficient access to data.
            Last-in, First-out (LIFO): Stacks follow the LIFO principle, ensuring that the last element added to the stack is the first one removed. This behavior is useful in many scenarios, such as function calls and expression evaluation.
            Limited memory usage: Stacks only need to store the elements that have been pushed onto them, making them memory-efficient compared to other data structures.
           
              Disadvantages of Stack Data Structure:
Limited access: Elements in a stack can only be accessed from the top, making it difficult to retrieve or modify elements in the middle of the stack.
Potential for overflow: If more elements are pushed onto a stack than it can hold, an overflow error will occur, resulting in a loss of data.
Not suitable for random access: Stack s do not allow for random access to elements, making them unsuitable for applications where elements need to be accessed in a specific order.
Limited capacity: Stacks have a fixed capacity, which can be a limitation if the number of elements that need to be stored is unknown or highly variable.


Applications of Stack Data Structure:
Infix to Postfix /Prefix conversion
Redo-undo features at many places like editors, photoshop.
Forward and backward features in web browsers
In Memory management, any modern computer uses a stack as the primary management for a running purpose. Each program that is running in a computer system has its own memory allocations.
Stack also helps in implementing function call in computers. The last called function is always completed first.




#
#
#

