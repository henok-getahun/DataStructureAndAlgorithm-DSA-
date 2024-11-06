from array import array

class ArrayOperations:
    def __init__(self, initial_data):
        self.arr = array('i', initial_data)

    def traversal(self):
        for x in self.arr:
            print(x, end=' ')
        print()

    def insertion(self, idx, val):
        n = len(self.arr)
        new_arr = array(self.arr.typecode, [0] * (n + 1))
        for i in range(idx):
            new_arr[i] = self.arr[i]
        new_arr[idx] = val
        for i in range(idx, n):
            new_arr[i + 1] = self.arr[i]
        self.arr = new_arr

    def deletion(self, val):
        idx = self.search(val)
        n = len(self.arr)
        if idx == -1:
            return
        new_arr = array(self.arr.typecode, [0] * (n - 1))
        for i in range(idx):
            new_arr[i] = self.arr[i]
        for i in range(idx, n - 1):
            new_arr[i] = self.arr[i + 1]
        self.arr = new_arr

    def search(self, val):
        n = len(self.arr)
        for i in range(n):
            if self.arr[i] == val:
                return i
        return -1

array_ops = ArrayOperations([1, 3, 5, 6, 7])


# array ds using list


class ArrayOperations:
    def __init__(self, initial_data):
        self.arr = initial_data 

    def traversal(self):
        for x in self.arr:
            print(x, end=' ')
        print()

    def insertion(self, idx, val):
        self.arr.insert(idx, val)  

    def deletion(self, val):
        idx = self.search(val)
        if idx != -1:
            self.arr.pop(idx) 

    def search(self, val):
        for i in range(len(self.arr)):
            if self.arr[i] == val:
                return i
        return -1

array_ops = ArrayOperations([1, 3, 5, 6, 7])


