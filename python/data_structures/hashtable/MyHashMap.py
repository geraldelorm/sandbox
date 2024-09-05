class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.bucket = [ListNode(0,0) for i in range(10**4)] 
        
    def put(self, key: int, value: int) -> None:
        curr = self.bucket[self.hashsum(key)]
        
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
            
        curr.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        curr = self.bucket[self.hashsum(key)]
        
        while curr.next:
            if curr.next.key == key:
                return curr.next.value
            
            curr = curr.next
        return -1
        

    def remove(self, key: int) -> None:
        curr = self.bucket[self.hashsum(key)]
        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
            
        
    def hashsum(self, key) -> None:
        return key % 10**4


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)