#---------[SBTree]---------

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    if rootNode is None:
        return BSTNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    return rootNode  


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
    queue = [rootNode]  
    while queue:
        currNode = queue.pop(0)
        print(currNode.data)
        if currNode.leftChild:
            queue.append(currNode.leftChild)
        if currNode.rightChild:
            queue.append(currNode.rightChild)


def searchNode(rootNode, target):
    if not rootNode:
        return False
    if target == rootNode.data:
        return True
    elif target < rootNode.data:
        return searchNode(rootNode.leftChild, target)
    else:
        return searchNode(rootNode.rightChild, target)


def deleteNode(rootNode, delValue):
    if not rootNode:
        return None  

    if delValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, delValue)
    elif delValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, delValue)
    else:
        # Node with only one child or no child
        if rootNode.leftChild is None:
            return rootNode.rightChild
        elif rootNode.rightChild is None:
            return rootNode.leftChild

        # Node with two children: Get the inorder successor
        temp = minNode(rootNode.rightChild)
        rootNode.data = temp.data  # Copy the inorder successor's value to this node
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)  # Delete the inorder successor

    return rootNode  # Return the modified tree


def minNode(node):
    currNode = node
    while currNode.leftChild:  # Traverse to the leftmost node of the right child of deleted node
        currNode = currNode.leftChild
    return currNode
