#--------[   ARRAY  ]-----------

from array import array

arr = array('i', [1, 3, 5, 6, 7])

def traversal(arr):
    for x in arr:
        print(x, end=' ')
    print()  

def insertion(arr, idx, val):
    n = len(arr)
    new_arr = array(arr.typecode, [0] * (n + 1))  
    for i in range(idx):
        new_arr[i] = arr[i]
    new_arr[idx] = val  
    for i in range(idx, n):
        new_arr[i + 1] = arr[i]
    return new_arr

def deletion(arr, val):
    idx = search(arr, val)
    n = len(arr)
    if idx == -1: 
        return arr  
    new_arr = array(arr.typecode, [0] * (n - 1))
    for i in range(idx):
        new_arr[i] = arr[i]
    for i in range(idx, n - 1):
        new_arr[i] = arr[i + 1]
    return new_arr

def search(arr, val):
    n = len(arr)
    for i in range(n):
        if arr[i] == val:  
            return i
    return -1


traversal(arr)
arr = insertion(arr, 2, 4)  
traversal(arr)
arr = deletion(arr, 5) 
traversal(arr)
