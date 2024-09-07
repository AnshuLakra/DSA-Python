# Binary Search Tree

from test import Queue


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertInBinarySearchTree(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BinarySearchTree(nodeValue)
        else:
            insertInBinarySearchTree(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BinarySearchTree(nodeValue)
        else:
            insertInBinarySearchTree(rootNode.rightChild, nodeValue)
    return "The Node is Successfully Inserted"


def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if rootNode is None:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if rootNode is None:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


# def searchBinarySearchTree(rootNode, value):
    # if rootNode is None:
    #     return
    # else:
    #     customQueue = Queue()
    #     customQueue.enqueue(rootNode)
    #     while not (customQueue.isEmpty()):
    #         root = customQueue.dequeue()
    #         if root.value.data == value:
    #             return "Success"
    #         if root.value.leftChild is not None:
    #             customQueue.enqueue(root.value.leftChild)
    #         if root.value.rightChild is not None:
    #             customQueue.enqueue(root.value.rightChild)
    #     return "Not Found"

def searchBinarySearchTree(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The Value is Found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The Value is Found")
        else:
            searchBinarySearchTree(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The Value is Found")
        else:
            searchBinarySearchTree(rootNode.rightChild, nodeValue)


def minValueNode(rootNode):
    if rootNode is None:
        return
    current = rootNode
    while current.leftChild is not None:
        current = current.leftChild
    return current

def deleteNode(rootNode,nodeValue):
    if rootNode is None:
        return 
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        minValue = minValueNode(rootNode.rightChild)
        rootNode.data = minValue.data
        rootNode.rightChild = deleteNode(rootNode.rightChild,minValue.data)
    return rootNode


def deleteBinaryTree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None    
    return "Binary Tree Deleted successfully"


bst = BinarySearchTree(None)
print(insertInBinarySearchTree(bst, 10))
print(insertInBinarySearchTree(bst, 5))
print(insertInBinarySearchTree(bst, 15))
print(insertInBinarySearchTree(bst, 4))
print(insertInBinarySearchTree(bst, 6))
print(insertInBinarySearchTree(bst, 1))
print(insertInBinarySearchTree(bst, 18))

# print(bst.rightChild.data)
# preOrderTraversal(bst)
# inOrderTraversal(bst)
# postOrderTraversal(bst)
# levelOrderTraversal(bst)
# searchBinarySearchTree(bst, 51)
# print(minValueNode(bst).data)

deleteNode(bst, 4)
levelOrderTraversal(bst)
# inOrderTraversal(bst)

