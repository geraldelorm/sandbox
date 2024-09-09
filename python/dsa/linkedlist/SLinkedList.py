class Node:
    def __init__(self, val, _next = None):
        self.val = val
        self.next = _next

class MyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def get(self, index : int) -> int:
        if index < 0 or index >= self.size:
            return - 1
        
        curr = self.head
        while index > 0:
            curr = curr.next
            index -= 1

        return curr.val


    def addAtHead(self, val: int) -> None:
        newNode = Node(val)

        if not self.head:
            self.head = newNode
        else:
            temp = self.head
            newNode.next = temp
            self.head = newNode

        self.size += 1


    def addAtTail(self, val: int) -> None: #improve
        newNode = Node(val)

        if not self.head:
            self.head = newNode
        else:
            curr = self.head

            while curr.next:
                curr = curr.next

            curr.next = newNode

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return 
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr = self.head

            for _ in range(index - 1):
                curr = curr.next

            newNode = Node(val)

            temp = curr.next
            curr.next = newNode
            newNode.next = temp
            

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 

        if index == 0 :
            self.head = self.head.next
        else:
            curr = self.head

            for _ in range(index - 1):
                curr = curr.next

            curr.next = curr.next.next

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)