# [BINARY HEAP]


class BinaryHeap:
    def __init__(self, capacity):
        self.currentSize = 0
        self.maxCapacity = capacity + 1
        self.elements = [None] * (self.maxCapacity + 1)


def topOfHeap(heap):
    if not heap or heap.currentSize == 0:
        return None
    return heap.elements[1]


def countOfHeap(heap):
    if not heap:
        return 0
    return heap.currentSize


def traverseLevelOrder(heap):
    if not heap:
        return
    for i in range(1, heap.currentSize + 1):
        print(heap.elements[i])


def bubbleUp(heap, index, heapType):
    parentIndex = index // 2
    if index <= 1:
        return

    if heapType == 'Min':
        if heap.elements[index] < heap.elements[parentIndex]:
            heap.elements[index], heap.elements[parentIndex] = heap.elements[parentIndex], heap.elements[index]
        bubbleUp(heap, parentIndex, heapType)
    elif heapType == 'Max':
        if heap.elements[index] > heap.elements[parentIndex]:
            heap.elements[index], heap.elements[parentIndex] = heap.elements[parentIndex], heap.elements[index]
        bubbleUp(heap, parentIndex, heapType)


def addNode(heap, value, heapType):
    if heap.currentSize + 1 == heap.maxCapacity:
        return 'Full'
    heap.elements[heap.currentSize + 1] = value
    heap.currentSize += 1
    bubbleUp(heap, heap.currentSize, heapType)


def bubbleDown(heap, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if leftIndex > heap.currentSize:
        return
    elif leftIndex == heap.currentSize:
        swapChild = leftIndex
    else:
        if heapType == "Min":
            swapChild = leftIndex if heap.elements[leftIndex] < heap.elements[rightIndex] else rightIndex
            if heap.elements[index] > heap.elements[swapChild]:
                heap.elements[index], heap.elements[swapChild] = heap.elements[swapChild], heap.elements[index]
        else:
            swapChild = leftIndex if heap.elements[leftIndex] > heap.elements[rightIndex] else rightIndex
            if heap.elements[index] < heap.elements[swapChild]:
                heap.elements[index], heap.elements[swapChild] = heap.elements[swapChild], heap.elements[index]

    bubbleDown(heap, swapChild, heapType)


def removeNode(heap, heapType):
    if heap.currentSize == 0:
        return None
    removedNode = heap.elements[1]
    heap.elements[1] = heap.elements[heap.currentSize]
    heap.elements[heap.currentSize] = None
    heap.currentSize -= 1
    bubbleDown(heap, 1, heapType)
    return removedNode


def clearHeap(heap):
    heap.elements = None
    heap.currentSize = 0
    heap.maxCapacity = 0
