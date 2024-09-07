# Queue data structure


# class Queue:
#     def __init__(self):
#         self.items = []

#     def __str__(self):
#         values = [str(x) for x in self.items]
#         return '<-'.join(values)
    

#     def isEmpyt(self):
#         if self.items == []:
#             return True
#         else:
#             return False
    
#     def enqueue(self, value):
#         self.items.append(value)
#         return "The element is inserted at end of Queue"
    
#     def dequeue(self):
#         if self.isEmpyt():
#             return "Queue is empty"
#         else:
#             return self.items.pop(0)



#     def peek(self):
#         if self.isEmpyt():
#             return "Queue is empty"
#         else:
#             return self.items[0]
    
#     def delete(self):
#         self.items = None




    
# customQueue = Queue()

# customQueue.enqueue(10)
# customQueue.enqueue(20)
# customQueue.enqueue(30)
# customQueue.dequeue()
# customQueue.enqueue(40)
# print(customQueue.peek())
# customQueue.delete()


# print(customQueue.peek())
# print(customQueue.isEmpyt())
# print(customQueue)


# Circular Queue


# class Queue:
#     def __init__(self,maxSize):
#         self.items = maxSize * [None]
#         self.maxSize = maxSize
#         self.start = -1
#         self.top = -1

#     def __str__(self):
#         values = [str(x) for x in self.items]
#         return ' '.join(values )
    
#     def isFull(self):
#         if self.top + 1 == self.start:
#             return True
#         elif self.start == 0 and self.top + 1 == self.maxSize:
#             return True
#         else:
#             return False 
    
#     def isEmpyt(self):
#         if self.top == -1:
#             return True
#         else:
#             return False
        
#     def enqueue(self, value):
#         if self.isFull():
#             return "Queue is Full"
#         else:
#             if self.top + 1 == self.maxSize:
#                 self.top = 0
#             else:
#                 self.top += 1
#                 if self.start == -1:
#                     self.start = 0
#             self.items[self.top] = value
#             return "The element is inserte at end of the queue"

    
#     def dequeue(self):
#         if self.isEmpyt():
#             return "Queue is empty"
#         else:
#             firstElement = self.items[self.start]
#             start = self.start
#             if self.start == self.top:
#                 self.start = -1
#                 self.top = -1
#             elif self.start + 1 == self.maxSize:
#                 self.start = 0
#             else:
#                 self.start += 1
#             self.items[start] = None
#             return firstElement

#     def peek(self):
#         if self.isEmpyt():
#             return "Queue is Empty"
#         else:
#             return self.items[self.start]
    
#     def delete(self):
#         self.items = self.maxSize * [None]
#         self.top = -1
#         self.start = -1



# customQueue = Queue(4)
# customQueue.enqueue(10)
# customQueue.enqueue(20)
# customQueue.enqueue(30)
# customQueue.enqueue(40)
# print(customQueue.dequeue())

# print(customQueue.isFull())


# print(customQueue)
# print(customQueue.peek())

# print(customQueue.isFull())
# print(customQueue.isEmpyt())


# Queue using LinkedList


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

#     def __str__(self):
#         return str(self.value)
    

# class LinkedList:
#     def __init__(self):
#         self.head = None 
#         self.tail = None
    
#     def __iter__(self):
#         temp = self.head
#         while temp:
#             yield temp
#             temp = temp.next
    

# class Queue:
#     def __init__(self):
#         self.linkedlist = LinkedList()

#     def __str__(self):
#         values = [str(x.value) for x in self.linkedlist]
#         return  ' '.join(values)

#     def enqueue(self, value):
#         new_node = Node(value)
#         if self.linkedlist.head == None:
#             self.linkedlist.head = new_node
#             self.linkedlist.tail = new_node
#         else:
#             self.linkedlist.tail.next = new_node
#             self.linkedlist.tail = new_node
#     def isEmpty(self):
#         if self.linkedlist.head == None:
#             return True
#         else:
#             return False

#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is Empty"
#         else:
#             temp = self.linkedlist.head
#             if self.linkedlist.head == self.linkedlist.tail:
#                 self.linkedlist.head = None
#                 self.linkedlist.tail = None
#             else:
#                 self.linkedlist.head = self.linkedlist.head.next
#             return temp
    
#     def peek(self):
#         if self.isEmpty():
#             return "queue is empty"
#         else:
#             return self.linkedlist.head
    
#     def delete(self):
#         self.linkedlist.head = None
#         self.linkedlist.tail = None


# customQueue  = Queue()

# customQueue.enqueue(10)
# customQueue.enqueue(20)
# customQueue.enqueue(30)
# customQueue.enqueue(40)
# print(customQueue.dequeue())
# customQueue.enqueue(50)


# print(customQueue)
# print(customQueue.peek())


# from Collections Module

# from collections import deque

# customQueue = deque(maxlen=3)

# customQueue.append(10)
# customQueue.append(20)
# customQueue.append(30)
# customQueue.append(40)
# print(customQueue)
# print(customQueue.popleft())
# print(customQueue.clear())
# print(customQueue)


# from Queue

# import queue as q

# customQueue = q.Queue(maxsize=3)
# print(customQueue.empty())
# print(customQueue.qsize())
# customQueue.put(1)
# customQueue.put(2)
# customQueue.put(3)
# print(customQueue.get())
# print(customQueue)


