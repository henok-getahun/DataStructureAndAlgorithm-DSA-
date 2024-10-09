#                                                                                       .......[ STACK ].......

#1 Stack With Fixed size List

class Stack:
    def __init__(self):
       self.stack =[]
       self.maxSize = 10

    def push(self, value):
        if len(self.stack) == self.maxSize-1:
            return 'stack overflow'
        else:
            self.stack.append(value)
            print(f'{value} is  pushed to stack')

    def pop(self):
        if self.isEmpty():
            return 'stack underflow'
        else:
            return self.stack.pop()

    def top(self):
        if self.isEmpty():
            return 'empty stack'
        else:
            return self.stack[len(self.stack) - 1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def isFull(self):
        if len(self.stack) == self.maxSize:
            return True
        else:
            return False



#2 Stack With LinkedList

class StackNode:
    def __int__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return True if self.top is None else False

    def push(self, value):
        newNode = StackNode(value)
        newNode.next = self.top
        self.top = newNode

    def peek(self):
        if self.isEmpty():
            return 'Empty stack!'
        return self.top.value

    def pop(self):
        if self.isEmpty():
            return 'no element to be popped'
        temp = self.top
        self.top = self.top.next
        return temp.value










