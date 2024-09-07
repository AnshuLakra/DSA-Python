class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class CLinkedlist:
    def __init__(self):
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
            result += ' -> '
        return result    


    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1
    
    def insert(self,value,index):
        new_node = Node(value)
        if index > self.length or index < 0:
            raise Exception("Index is out of range")
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.tail.next = new_node
                self.head = new_node
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break
    
    def search(self,value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            if temp == self.head:
                break
            temp = temp.next
        return False
    
    def get(self,index):
        temp = self.head
        if index < -1 or index >= self.length:
            return None
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
        
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            popped_node = self.tail
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove(self,index):
        temp = self.head
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        for _ in range(index-1):
            temp = temp.next
        popped_node = temp.next
        temp.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def delete(self):
        if self.length == 0:
            return None
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0
        return None


cl = CLinkedlist()

cl.append(10)
cl.append(20)
cl.append(30)
cl.prepend(100) 
cl.insert(200,0)

print(cl)
# print(cl.tail.next.value)
# print(cl.length)
# cl.traverse()
# print(cl.search(1000))
# print(cl.get(1000))
# print(cl.set_value(1,999))
# print(cl.pop_first().value)
# print(cl.pop().value)
# print(cl.remove(4))
print(cl.delete())
print(cl.length)
print(cl.delete())

# print(cl.tail.value)
