class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Hash:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.hashTable = [None] * capacity
        self.size = 0

    def hash_function(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        if self.size == self.capacity:
            raise ValueError('hash is full')
        idx = self.hash_function(key)
        head = self.hashTable[idx]
        while head:
            if key == head.key:
                head.value = value
                return
            head = head.next
        newNode = Node(key, value)
        newNode.next = self.hashTable[idx]
        self.hashTable[idx] = newNode
        self.size += 1

    def search(self, key):
        idx = self.hash_function(key)
        head = self.hashTable[idx]
        while head:
            if key == head.key:
                return True
            head = head.next
        return False

    def remove(self, key):
        idx = self.hash_function(key)
        head = self.hashTable[idx]
        prev = None

        while head:
            if key == head.key:
                if prev:
                    prev.next = head.next
                else:
                    self.hashTable[idx] = head.next
                self.size -= 1
                return
            prev = head
            head = head.next


newHash = Hash()

