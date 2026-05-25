'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
'''
class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next

class singleLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insertAtBegin(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
    
    def insertAtEnd(self, value):
        temp = Node(value)
        
        if (self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
    
    def insertAtMiddle(self, value, x):
        temp = Node(value)
        t1= self.head

        while(t1.next != None):
            if(t1.info == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next
        
    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.info, end = " -> ")
            t1 = t1.next
        print(t1.info)

    

ll = singleLinkedList()
ll.insertAtBegin(12)
ll.insertAtEnd(14)
ll.insertAtMiddle(13,12)

ll.printLL()