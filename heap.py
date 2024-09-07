

class BinaryHeap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

    def __str__(self):
        values = [str(x) for x in self.customList]
        return ' '.join(values)


def peekOfHeap(rootNode):
    if rootNode is None:
        return
    else:
        return rootNode.customList[1]


def sizeOfHeap(rootNode):
    if rootNode is None:
        return
    else:
        return rootNode.heapSize


def preOrderTraversal(rootNode, index):
    if index > rootNode.heapSize:
        return
    else:
        print(rootNode.customList[index])
        preOrderTraversal(rootNode, (index * 2))
        preOrderTraversal(rootNode, (index * 2 + 1))


def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[1])


def heapify(rootNode, index, heapType):
    parentNode = int(index/2)
    if index <= 1:
        return
    if heapType == 'min':
        if rootNode.customList[index] < rootNode.customList[parentNode]:
            tmp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentNode]
            rootNode.customList[parentNode] = tmp
        heapify(rootNode, parentNode, heapType)
    if heapType == 'max':
        if rootNode.customList[index] > rootNode.customList[parentNode]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentNode]
            rootNode.customList[parentNode] = temp
        heapify(rootNode, parentNode, heapType)


def insertInBinaryHeap(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Heap is Full"
    else:
        rootNode.customList[rootNode.heapSize + 1] = nodeValue
        rootNode.heapSize += 1
        heapify(rootNode, rootNode.heapSize, heapType)
        return "The node is Inserted"


def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0
    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == 'min':
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heapType == 'min':
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyTreeExtract(rootNode, swapChild, heapType)

def extractNode(rootNode,heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode,1,heapType)
        return extractedNode

def deleteHeap(rootNode):
    rootNode.customList = None




bHeap = BinaryHeap(5)
insertInBinaryHeap(bHeap, 40, 'min')
insertInBinaryHeap(bHeap, 50, 'min')
insertInBinaryHeap(bHeap, 30, 'min')
insertInBinaryHeap(bHeap, 10, 'min')
insertInBinaryHeap(bHeap, 20, 'min')

extractNode(bHeap,'min')

# print(peekOfHeap(bHeap))
# print(sizeOfHeap(bHeap))
# preOrderTraversal(bHeap, 1)
# levelOrderTraversal(bHeap)
print(bHeap)

