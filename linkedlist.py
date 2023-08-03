class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def addnode(self, new_val):
        new_node = Node(new_val)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
        self.head = new_node
    def printnode(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            val = self.head
            while val != None:
                print(str(val.value) + "----->", end='')
                val = val.next
    def deletenode(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            self.head = self.head.next

s1 = LinkedList()
s1.addnode(7)
s1.addnode(9)
s1.addnode(8)
s1.addnode(5)
s1.printnode()
s1.deletenode()
print("\nprinting the node after deleting it")
s1.printnode()