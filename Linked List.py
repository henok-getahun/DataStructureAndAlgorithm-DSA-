#                               -----[lINKED LIST]------


#1      SINGLY LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

   def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_after(self, prev_data, data):
        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node with data {prev_data} not found.")

    def delete_node(self, key):
        current = self.head
        prev = None

        
        if not current:
            print("The list is empty.")
            return

        
        if current.data == key:
            self.head = current.next
            current = None
            return

        
        while current and current.data != key:
            prev = current
            current = current.next

        
        if current is None:
            print(f"Node with data {key} not found.")
            return
        prev.next = current.next
        current = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



#2           DOUBLY LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def insert_after(self, prev_data, data):
        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(data)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next
        print(f"Node with data {prev_data} not found.")
      

    def delete_node(self, key):
        current = self.head

        if not current:
            print("The list is empty.")
            return

        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  
                    self.head = current.next
                current = None
                return
            current = current.next

        print(f"Node with data {key} not found.")

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def display(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")




#3      CIRCULAR LINKED LIST



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node  
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node  
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete_node(self, key):
        if not self.head:
            print("The list is empty.")
            return

        current = self.head
        prev = None

        while True:
            if current.data == key:
                if current == self.head:  
                    if current.next == self.head:  
                        self.head = None
                    else:
                        prev = self.head
                        while prev.next != self.head:
                            prev = prev.next
                        prev.next = current.next
                        self.head = current.next
                else:
                    prev.next = current.next
                current = None
                return
            prev = current
            current = current.next
            if current == self.head:
                break

        print(f"Node with data {key} not found.")

    def search(self, key):
        if not self.head:
            return False
        current = self.head
        while True:
            if current.data == key:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def traverse(self):
        elements = []
        if not self.head:
            return elements
        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        return elements

    def display(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")



  

