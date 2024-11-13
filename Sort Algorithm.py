import math
def bubbleSort( customList):
    n = len(customList)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if customList[i] > customList[j]:
                customList[i], customList[j] = customList[j], customList[i]
    return customList


def selectionSort( customList):
    n = len(customList)
    for i in range(n):
        minIdx = i
        for j in range(i + 1, n):
            if customList[minIdx] > customList[j]:
                minIdx = j
        customList[i], customList[minIdx] = customList[minIdx], customList[i]

    return customList


def insertionSort(customList):
    n = len(customList)
    for i in range(1, n):
        key = customList[i]
        j = i - 1
        while j >= 0 and customList[j] > key:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return customList


def bucketSort(customList):
    n = len(customList)
    bucketsNumber = round(math.sqrt(n))
    buckets = []
    maxElement = max(customList)
    for i in range(bucketsNumber):
        buckets.append([])
    for item in customList:
        bucketIdx = math.ceil(item * bucketsNumber / maxElement) - 1
        if bucketIdx < 0:
            bucketIdx = 0
        buckets[bucketIdx].append(item)
    for i in range(bucketsNumber):
        buckets[i] = bubbleSort(buckets[i])

    k = 0
    for i in range(bucketsNumber):
        for j in range(len(buckets[i])):
            customList[k] = buckets[i][j]
            k += 1
    return customList


def mergeSort(customList):
   if len(customList) > 1:

       leftList = customList[:len(customList)//2]
       rightList = customList[len(customList)//2:]
       mergeSort(leftList)
       mergeSort(rightList)

       i = 0
       j = 0
       k = 0

       while i < len(leftList) and j < len(rightList):
           if leftList[i] < rightList[j]:
               customList[k] = leftList[i]
               i += 1
           else:
               customList[k] = rightList[j]
               j += 1
           k += 1
       while i < len(leftList):
           customList[k] = leftList[i]
           i += 1
           k += 1

       while j < len(rightList):
           customList[k] = rightList[j]
           j += 1
           k += 1

   return customList


def partition(customList, startIdx, endIdx):
    swapIdx = pivotIdx = startIdx
    for i in range(startIdx + 1, endIdx + 1):
        if customList[pivotIdx] > customList[i]:
            swapIdx += 1
            customList[swapIdx], customList[i] = customList[i], customList[swapIdx]
    customList[pivotIdx], customList[swapIdx] = customList[swapIdx], customList[pivotIdx]

    return swapIdx


def quickSort(customList, startIdx=0, endIdx=None):
    if endIdx is None:
        endIdx = len(customList) - 1
    if startIdx < endIdx:
        pivotIdx = partition(customList, startIdx, endIdx)
        quickSort(customList, startIdx, pivotIdx-1)
        quickSort(customList, pivotIdx+1, endIdx)
    return customList


class MinHeap:
    def __init__(self, capacity=10):
        self.maxCapacity = capacity
        self.currentSize = 0
        self.elements = [None] * (self.maxCapacity + 1)

    def heapify_up(self, idx):

        parentIdx = idx // 2
        if idx <= 1:
            return
        if self.elements[parentIdx] > self.elements[idx]:
            self.elements[parentIdx], self.elements[idx] = self.elements[idx], self.elements[parentIdx]
            self.heapify_up(parentIdx)

    def heapify_down(self, idx):

        smallest = idx
        left = 2 * idx
        right = 2 * idx + 1

        if left <= self.currentSize and self.elements[left] < self.elements[smallest]:
            smallest = left

        if right <= self.currentSize and self.elements[right] < self.elements[smallest]:
            smallest = right

        if smallest != idx:
            self.elements[idx], self.elements[smallest] = self.elements[smallest], self.elements[idx]
            self.heapify_down(smallest)

    def addNode(self, value):
        if self.currentSize >= self.maxCapacity:
            raise Exception('The heap is already full')
        self.currentSize += 1
        self.elements[self.currentSize] = value
        self.heapify_up(self.currentSize)

    def extract(self):
        if self.currentSize == 0:
            raise Exception('Empty heap')
        rootNode = self.elements[1]
        self.elements[1] = self.elements[self.currentSize]
        self.currentSize -= 1
        self.heapify_down(1)
        return rootNode


def heapSort(arr):
    min_heap = MinHeap(len(arr))

    for value in arr:
        min_heap.addNode(value)

    sorted_array = []
    for _ in range(len(arr)):
        sorted_array.append(min_heap.extract())

    return sorted_array





























# unsortedList = [5, 3, 6, 2, 0, 15, 20]
# print(mergeSort(unsortedList))
#
# print(bubbleSort(unsortedList))
# print(selectionSort(unsortedList))
# print(insertionSort(unsortedList))
# print(bucketSort(unsortedList))




