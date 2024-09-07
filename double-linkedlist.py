
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    # def __str__(self):
    #     return str(self.value)
    #     return f"{self.prev} <- {self.value} -> {self.next}"

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        result = ''
        temp = self.head
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += " <-> "
            temp = temp.next
        return result
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    
    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def prev_traverse(self):
        temp = self.tail
        while temp is not None:
            print(temp.value)
            temp = temp.prev
    
    def search(self,target):
        temp = self.head
        index = 0
        while temp is not None:
            if temp.value == target:
                return index
            temp = temp.next
            index += 1
        return -1
    
    def get(self,index):
        if index >= self.length or index < 0:
            return None
        if index < self.length // 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1 ,index,-1):
                temp = temp.prev
        return temp
    
    def set(self,index,value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        temp = self.head
        new_node = Node(value)
        if index > self.length or index < 0:
            return None
        if index == 0:
            # new_node.next = self.head
            # self.head.prev = new_node
            # self.head = new_node
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            new_node.prev = temp
            temp.next = new_node
            temp.next.prev = new_node
            self.length += 1
        
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        else:
            self.head = self.head.next
            self.head.pre = None
            popped_node.next = None
        self.length -= 1
        return popped_node
        
    def pop(self):
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        elif self.length == 0:
            return None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node

    def remove(self,index):
        # temp = self.get(index-1)
        # popped_node = temp.next
        # temp.next = popped_node.next
        # popped_node.next.pre = temp
        # popped_node.next = None
        # popped_node.pre = None
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

            


# new_node = Node(10)
# print(new_node)


cl = DLinkedList()

cl.append(10)
cl.append(20)
cl.append(30)
cl.append(40)
cl.append(50)
cl.prepend(111)

print(cl)
# print(cl.length)
# print(cl.set(2,999))
# cl.insert(3,999)
# print(cl.pop_first().value)
# print(cl.pop())

cl.remove(5)

print(cl)
# print(cl.length)


# print(cl.get(2).value)


# print(cl.search(50))


# cl.traverse()
# cl.prev_traverse()

# print(cl.tail.prev.value)

