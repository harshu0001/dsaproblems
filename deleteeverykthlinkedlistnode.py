'''
Given a singly linked list, remove every k‑th node from the list (using 1‑based indexing).
 It is guaranteed that **k** is less than or equal to the length of the list. After removal, 
 the remaining nodes should stay in their original order.

Example 1:
Input:  List: 1 → 2 → 3 → 4 → 5 → 6,  k = 2
Output: 1 → 3 → 5
Explanation: Every 2nd node (2, 4, 6) is removed, leaving 1, 3, and 5.

Example 2:
Input:  List: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10,  k = 3
Output: 1 → 2 → 4 → 5 → 7 → 8 → 10
Explanation: Nodes at positions 3, 6, and 9 (values 3, 6, 9) are removed.
'''

class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next

class Singlylinkedlist:
    def __init__(self,head=None):
        self.head = head
    
    def insertAtBegin(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
    
    def insertAtEnd(self, value):
        temp = Node(value)
        t1 = self.head

        while(t1.next!= None):
            t1 = t1.next
        t1.next = temp

    
    def printLL(self):
        t1 = self.head
        while (t1.next!=None):
            print(t1.info, end = " ")
            t1 = t1.next
        print(t1.info)

    def deleteNthNode(self, k):
        l = 0
        t1 = self.head
        while(t1!= None):
            t1 = t1.next
            l+=1

        # print(t1.info)

        for i in range(0,l-1,k):
            while(t1!= None):
                t1 = t1.next
            print(t1.info)


obj = Singlylinkedlist()
obj.insertAtBegin(10)
obj.insertAtEnd(11)
obj.insertAtEnd(12)
obj.insertAtEnd(13)
obj.deleteNthNode(2)
# obj.printLL()
