
# class TreeNode:
#     def __init__(self, data, children=[]):
#         self.data = data
#         self.children = children

#     def __str__(self, level=0):
#         let = " " * level + str(self.data) + "\n"
#         for child in self.children:
#             let += child.__str__(level + 1)
#         return let

#     def addchild(self, TreeNode):
#         self.children.append(TreeNode)


# rootTree = TreeNode("Drinks",[])
# hot = TreeNode("Hot",[])
# cold = TreeNode("Cold",[])

# rootTree.addchild(hot)
# rootTree.addchild(cold)

# tea = TreeNode("tea",[])
# hot.addchild(tea)
# print(rootTree)


# from test import Queue


# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None


# drinks = TreeNode('Drinks')
# hot = TreeNode('Hot')
# cold = TreeNode('Cold')

# drinks.leftChild = hot
# drinks.rightChild = cold

# tea = TreeNode('Tea')
# hot.leftChild = tea
# coffee = TreeNode('Coffee')
# hot.rightChild = coffee

# cola = TreeNode('Cola')
# cold.rightChild = cola

# print('\nPre Order Traversal\n')


# def preOrderTraversal(rootNode):
#     if rootNode is None:
#         return
#     print(rootNode.data)
#     preOrderTraversal(rootNode.leftChild)
#     preOrderTraversal(rootNode.rightChild)


# preOrderTraversal(drinks)

# print("\nIn Order Traversal\n")


# def inOrderTraversal(rootNode):
#     if rootNode is None:
#         return
#     inOrderTraversal(rootNode.leftChild)
#     print(rootNode.data)
#     inOrderTraversal(rootNode.rightChild)


# inOrderTraversal(drinks)

# print("\nPost Order Traversal\n")


# def postOrderTraversal(rootNode):
#     if rootNode is None:
#         return
#     postOrderTraversal(rootNode.leftChild)
#     postOrderTraversal(rootNode.rightChild)
#     print(rootNode.data)


# postOrderTraversal(drinks)


# print("\nLevel Order Traversal\n")


# def levelOrderTraversal(rootNode):
#     if rootNode is None:
#         return
#     else:
#         customQueue = Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             print(root.value.data)
#             if (root.value.leftChild is not None):
#                 customQueue.enqueue(root.value.leftChild)
#             if (root.value.rightChild is not None):
#                 customQueue.enqueue(root.value.rightChild)


# levelOrderTraversal(drinks)

# print('\nBinary Search Tree\n')


# def searchBinaryTree(rootNode, nodeValue):
#     if rootNode is None:
#         return "The Node value does not Exist"
#     else:
#         customQueue = Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             if root.value.data == nodeValue:
#                 return "Success"
#             else:
#                 if (root.value.leftChild is not None):
#                     customQueue.enqueue(root.value.leftChild)
#                 if (root.value.rightChild is not None):
#                     customQueue.enqueue(root.value.rightChild)
#         return "UnsuccessFull"


# print(searchBinaryTree(drinks, 'Cola'))


# def insertNodeInBinaryTree(rootNode, newNode):
#     if rootNode is None:
#         rootNode = newNode
#     else:
#         customQueue = Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)
#             else:
#                 root.value.leftChild = newNode
#                 return "Success inserted in Left"
#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)
#             else:
#                 root.value.rightChild = newNode
#                 return "Success inserted in Right"


# newNode = TreeNode("New")
# insertNodeInBinaryTree(drinks, newNode)

# levelOrderTraversal(drinks)


# def getDeepestNode(rootNode):
#     if rootNode is None:
#         return
#     else:
#         customQueue = Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)
#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)
#         deepestNode = root.value
#         return deepestNode


# deepestNode = getDeepestNode(drinks)
# print(deepestNode.data)


# def deleteDeepestNode(rootNode, dNode):
#     if rootNode is None:
#         return
#     else:
#         customQueue = Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             if root.value == dNode:
#                 root.value = None
#                 return
#             if root.value.leftChild is not None:
#                 if root.value.leftChild == dNode:
#                     root.value.leftChild = None
#                     return
#                 else:
#                     customQueue.enqueue(root.value.leftChild)
#             if root.value.rightChild is not None:
#                 if root.value.rightChild == dNode:
#                     root.value.rightChild = None
#                     return
#                 else:
#                     customQueue.enqueue(root.value.rightChild)


# deepestNode = getDeepestNode(drinks)
# levelOrderTraversal(drinks)
# deleteDeepestNode(drinks,deepestNode)
# levelOrderTraversal(drinks)

# def deleteNodeBT(rootNode, node):
#     if rootNode is None:
#         return
#     else:
#         customQueue = Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             if root.value.data == node:
#                 dNode = getDeepestNode(rootNode)
#                 root.value.data = dNode.data
#                 deleteDeepestNode(rootNode, dNode)
#                 return "The node has been successfully deleted"
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)
#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)


# levelOrderTraversal(drinks)
# print(deleteNodeBT(drinks,'Tea'))
# levelOrderTraversal(drinks)


# def deleteBinaryTree(rootNode):
#     rootNode.data = None
#     rootNode.leftChild = None
#     rootNode.rightChild = None
#     return "Binary Treee is deleted"


# Binary Tree Using List


class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastIndexUsed = 0
        self.maxSize = size

    def __str__(self):
        values = [str(x) for x in self.customList]
        return ' '.join(values)

    def insert(self, value):
        if self.lastIndexUsed + 1 == self.maxSize:
            return "The binary Tree is Full"
        else:
            self.customList[self.lastIndexUsed + 1] = value
            self.lastIndexUsed += 1
            return "The value is Inserted"

    def search(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Found"
        return "Not Found"

    def preOrderTraversal(self, index):
        if index > self.lastIndexUsed:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastIndexUsed:
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self, index):
        if index > self.lastIndexUsed:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in range(1, self.lastIndexUsed + 1):
            print(self.customList[i])

    def deleteNode(self,value):
        if self.lastIndexUsed == 0:
            return "Tree is Empty"
        for i in range(1,self.lastIndexUsed+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastIndexUsed]
                self.customList[self.lastIndexUsed] = None
                self.lastIndexUsed -= 1
                return "Node is deleted"
        
    def deleleBinaryTree(self):
        self.customList = None
        return "The Binary tree is deleted successfull"
    




bTree = BinaryTree(5)
print(bTree.insert('Drinks'))
print(bTree.insert('Hot'))
print(bTree.insert('Cold'))
print(bTree.insert('Tea'))
print(bTree.insert('Coffee'))

print(bTree)
print("\nPreOrderTraversal")
bTree.preOrderTraversal(1)
print("\nInOrderTraversal")
bTree.inOrderTraversal(1)
print('\nPostOrderTraversal')
bTree.postOrderTraversal(1)
print('\nLevelOrderTraversal')
bTree.levelOrderTraversal(1)

print(bTree.deleteNode('Cold'))
bTree.levelOrderTraversal(1)

