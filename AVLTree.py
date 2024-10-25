class AVLNode:
    def __init__(self, nodeVal):
        self.data = nodeVal
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    Queue = [rootNode]
    while Queue:
        firstNode = Queue.pop(0)
        print(firstNode.data)
        if firstNode.leftChild:
            Queue.append(firstNode.leftChild)
        if firstNode.rightChild:
            Queue.append(firstNode.rightChild)


def searchNode(rootNode, target):
    if not rootNode:
        return False
    if target == rootNode.data:
        return True
    elif target < rootNode.data:
        return searchNode(rootNode.leftChild, target)
    else:
        return searchNode(rootNode.rightChild, target)


def getNodeHeight(unbalancedNode):
    if not unbalancedNode:
        return 0
    return unbalancedNode.height


def getNodeHeightDiff(rootNode):
    if not rootNode:
        return 0
    return getNodeHeight(rootNode.leftChild) - getNodeHeight(rootNode.rightChild)


def rightRotation(unbalancedNode):
    tempRoot = unbalancedNode.leftChild
    unbalancedNode.leftChild = tempRoot.rightChild
    tempRoot.rightChild = unbalancedNode

    # Update heights
    unbalancedNode.height = 1 + max(getNodeHeight(unbalancedNode.leftChild),
                                    getNodeHeight(unbalancedNode.rightChild))
    tempRoot.height = 1 + max(getNodeHeight(tempRoot.leftChild),
                              getNodeHeight(tempRoot.rightChild))

    return tempRoot


def leftRotation(unbalancedNode):
    tempRoot = unbalancedNode.rightChild
    unbalancedNode.rightChild = tempRoot.leftChild
    tempRoot.leftChild = unbalancedNode

    # Update heights
    unbalancedNode.height = 1 + max(getNodeHeight(unbalancedNode.leftChild),
                                    getNodeHeight(unbalancedNode.rightChild))
    tempRoot.height = 1 + max(getNodeHeight(tempRoot.leftChild),
                              getNodeHeight(tempRoot.rightChild))

    return tempRoot


def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    if nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    else:
        return rootNode  # Duplicate values are not allowed

    rootNode.height = 1 + max(getNodeHeight(rootNode.leftChild), getNodeHeight(rootNode.rightChild))

    balancefactor = getNodeHeightDiff(rootNode)

    # Left Left Case
    if balancefactor > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotation(rootNode)

    # Left Right Case
    if balancefactor > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)

    # Right Right Case
    if balancefactor < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotation(rootNode)

    # Right Left Case
    if balancefactor < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)

    return rootNode


def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)


def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode

    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)

    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)

    else:
        if not rootNode.leftChild:
            return rootNode.rightChild

        elif not rootNode.rightChild:
            return rootNode.leftChild

        tempNode = getMinValueNode(rootNode.rightChild)
        rootNode.data = tempNode.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, tempNode.data)


    rootNode.height = 1 + max(getNodeHeight(rootNode.leftChild), getNodeHeight(rootNode.rightChild))

    balanceFactor = getNodeHeightDiff(rootNode)

  
    if balanceFactor > 1 and getNodeHeight(rootNode.leftChild) >= 0:
        return rightRotation(rootNode)
    if balanceFactor < -1 and getNodeHeight(rootNode.rightChild) >= 0:
        return leftRotation(rootNode)
    if balanceFactor > 1 and getNodeHeight(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balanceFactor < -1 and getNodeHeight(rootNode.rightChild) < 0:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)

    return rootNode


def deleteAVL(rootNode):

    if rootNode:
        deleteAVL(rootNode.leftChild)
        deleteAVL(rootNode.rightChild)
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None
