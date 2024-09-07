
from random import randint

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class CDLinkedlistProblem:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0

    def __str__(self):
        result = ''
        temp = self.head
        while temp is not None:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += " <-> "
        return result
    
    def __len__(self):
        temp = self.head
        result = 0
        while temp is not None:
            result += 1
            temp = temp.next
            if temp == self.head:
                break
        return result
    
    def add(self,value):
        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        self.lenght += 1

    def generate(self,n,minValue,maxValue):
        self.head = None
        self.tail = None

        for _ in range(n):
            self.add(randint(minValue,maxValue))
        return self





cld = CDLinkedlistProblem()
cld.generate(5,0,99)
print(len(cld))
print(cld)

