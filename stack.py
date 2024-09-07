# Stack operations
# - creation
# - push
# - pop 
# - peek 
# - isEmpty
# - isFull 
# - deleteStack




# without limit

# class Stack:
#     def __init__(self):
#         self.list = []

#     def __str__(self):
#         values = [str(x) for x in reversed(self.list)]
#         return '\n'.join(values)


#     # isEmpty
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False
#     # push 
#     def push(self,value):
#         self.list.append(value)
#         return "The element has been successfully inserted"
    
#     def pop(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.list.pop()
        
#     def peek(self):
#         if self.isEmpty():
#             return "Empty stack"
#         else:
#             return self.list[len(self.list)-1]
    
#     def delete(self):
#         self.list = None
    

# cStack = Stack()
# cStack.push(10)
# cStack.push(20)
# cStack.push(30)
# # print(cStack.pop())
# # print(cStack.isEmpty())
# print(cStack)
# print(cStack.peek())


# with limit

# class Stack:
#     def __init__(self,maxSize):
#         self.maxSize = maxSize
#         self.list = []

#     def __str__(self):
#         values = [str(x) for x in reversed(self.list)]
#         return '\n'.join(values)
    
#     # isEmpty
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False
        
#     # isFull
#     def isFull(self):
#         if len(self.list) == self.maxSize:
#             return True
#         else:
#             return False


#     # push
#     def push(self,value):
#         if self.isFull():
#             return "Stack is full"
#         else:
#             self.list.append(value)
#             return "The element inserted successfull"
    
#     def pop(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.list.pop()
    
#     def peek(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.list[len(self.list) - 1]
    
#     def delete(self):
#         self.list = None
        
    
        

# cStack = Stack(4)
# print(cStack.isFull())
# print(cStack.isEmpty())
# cStack.push(10)
# cStack.push(20)
# cStack.push(30)
# cStack.push(40)
# print(cStack.push(50))
# print(cStack.peek())
# print(cStack)



# Stack using LinkedList

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.LinkeList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.LinkeList]
        return '\n'.join(values)
    
    def isEmpyt(self):
        if self.LinkeList.head == None:
            return True
        else:
            return False
    
    def push(self,value):
        node = Node(value)
        node.next = self.LinkeList.head
        self.LinkeList.head = node
    
    def pop(self):
        if self.isEmpyt():
            return "Stack is Empty"
        else:
            nodeValue = self.LinkeList.head.value
            self.LinkeList.head = self.LinkeList.head.next
            return nodeValue
    
    def peek(self):
        if self.isEmpyt():
            return "Empty"
        else:
            return self.LinkeList.head.value
        
    def delete(self):
        self.LinkeList.head = None
        
    

customStack = Stack()
customStack.push(10)
customStack.push(20)
customStack.push(30)
customStack.delete()
print(customStack.pop())
print(customStack)
print(customStack.peek())
print(customStack.isEmpyt())