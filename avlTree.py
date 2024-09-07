# AVL Tree
from test import Queue


class AVLTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


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


def searchAVLTree(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        return "Found"
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            return "Found"
        else:
            searchAVLTree(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            return "Found"
        else:
            searchAVLTree(rootNode.rightChild, nodeValue)


def getHeight(rootNode):
    if rootNode is None:
        return
    else:
        return rootNode.height

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot


def getBalance(rootNode):
    if rootNode is None:
        return
    else:
        return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)
    
def insertAVLTree(rootNode,nadeValue):
    




avlTree = AVLTree(10)
