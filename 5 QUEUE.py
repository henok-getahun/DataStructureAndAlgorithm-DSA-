#             -------[QUEUE]----------

# 1, IMPLEMENTATION USING ARRAY DATA STRUCTURE

class QueueArray:
    def __init__(self, Capacity):
        self.front = self.size = 0
        self.capacity = Capacity
        self.queue = [None]*Capacity
        self.rear = Capacity - 1

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def EnQueue(self, value):
        if self.isFull():
            print('Full')
            return
        self.rear = (self.rear + 1)% self.capacity
        self.queue[self.rear] = value
        self.size += 1
        print(f'{value} is enqueued.')

    def DeQueue(self):
        if self.isEmpty():
            print('Empty')
            return
        temp = self.queue[self.front]
        self.queue[self.front] = None
        self.size -= 1
        self.front = (self.front + 1) % self.capacity
        return print(f'{temp} is dequeued.')

    def que_front(self):
        if self.isEmpty():
            print('Empty')
            return
        return self.queue[self.front]

    def que_rear(self):
        if self.isEmpty():
            print('Empty')
            return
        return self.queue[self.rear]


# 2, IMPLEMENTATION USING LinkedList DATA STRUCTURE

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.rear = None
        self.front = None

    def isEmpty(self):
        return self.rear is None

    def EnQueue(self,value):
        newNode = Node(value)
        if self.isEmpty():
            self.rear = newNode
            self.front = newNode

        self.rear.next = newNode
        self.rear = newNode
        print(f'{value} is enqueued.')
        return

    def DeQueue(self):
        if self.isEmpty():
            print('Empty')
            return

        temp = self.front
        self.front = self.front.next
        print(f'{temp.value} is dequeued.')
        
        if self.front is None:
            self.rear = None
        return

    def QueFirst(self):
        if self.isEmpty():
            print('Empty')
            return
        print(self.front.value)
        return

    def QueLast(self):
        if self.isEmpty():
            print('Empty')
            return
        print(self.rear.value)
        return








    





