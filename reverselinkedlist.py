class Node:
    def __init__(self, info, next = None):
        self.info = info
        self.next = next


class singlyLinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def insertAtBegin(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
    
    def insertAtEnd(self, value):
        temp = Node(value)
        t1 = self.head
        if (self.head != None):
            while (t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertAtMiddle(self, value, x):
        temp = Node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.info == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next


    
    # def reverseLL(self):
    #     temp = self.head
    #     prev = None

    #     while(temp != None):
    #         front = temp.next
    #         temp.next = prev
    #         prev = temp
    #         temp = front

    def llmiddle(self):
        temp = self.head
        l = 0
        while (temp != None):
            temp = temp.next
            l+=1

        temp = self.head
        for i in range(l//2):
            temp = temp.next
        print(temp.info)

        
    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.info, end =" -> ")
            t1 = t1.next
        print(t1.info)

    
        

obj = singlyLinkedList()
obj.insertAtBegin(12)
obj.insertAtBegin(11)
obj.insertAtBegin(10)
obj.insertAtEnd(13)
obj.insertAtEnd(15)
obj.insertAtMiddle(14,13)
# obj.reverseLL()
obj.llmiddle()
# obj.printLL()
