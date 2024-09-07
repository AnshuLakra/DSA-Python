
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoubleLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = ''
        temp = self.head
        while temp is not None:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += ' <-> '
        return result
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            self.head = new_node
        self.length += 1
            
    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break

    def pretraverse(self):
        temp = self.tail
        while temp is not None:
            print(temp.value)
            temp = temp.prev
            if temp == self.tail:
                break

    def search(self,value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def get(self, index):
        if index >= self.length or index < 0:
            return None
        temp = None
        if index < self.length // 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index,-1):
                temp = temp.prev
        return temp
    
    def set(self,index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    

    def insert(self,index,value):
        if index > self.length or index < 0:
            print("Error: Index of bounds")
            return None
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            temp = self.get(index - 1)
            new_node = Node(value)
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node
        self.length += 1
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        else:
            self.head = self.head.next
            popped_node.next = None
            popped_node.prev = None
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1
        return popped_node

    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            popped_node.next = None
            popped_node.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1
        return popped_node
    
    def remove(self,index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            self.pop_first()
        elif index == self.length -1:
            self.pop()
        else:
            temp = self.get(index -1)
            popped_node = temp.next
            temp.next = popped_node.next
            popped_node.next.prev = temp
            popped_node.next = None
            popped_node.prev = None
            return popped_node
        self.length -= 1

    def delete(self):
        # if self.length == 0:
        #     return None
        # self.head.prev = None
        # self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0




t1 = CircularDoubleLinkedList()

t1.append(10)
t1.append(20)
t1.append(30)
t1.append(999)
t1.append(40)

# print(t1)
# print(t1.length)
# t1.prepend(999)
# t1.traverse()
# t1.pretraverse()

# print(t1.search(999))

print(t1)
print(t1.length)
# print(t1.get(3).value)
# print(t1.set(1,888))
# t1.insert(5,111)
# print(t1.pop_first().value)
# print(t1.pop().value)
# print(t1.remove(3))
t1.delete()
print(t1)
print(t1.length)
# print(t1.length)


# print(t1.tail.value)


