class MyHashSet:

    def __init__(self):
        self.bucket = [[]] * 5 
        self.bucket_size = 5 
        
        
    def hash_func(self, key: int) -> int:
        key_hash = key % self.bucket_size
        return key_hash
        

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        key_hash = self.hash_func(key)
        self.bucket[key_hash].append(key)
        

    def remove(self, key: int) -> None:
        if self.contains(key):
            key_hash = self.hash_func(key)
            if key in self.bucket[key_hash]:
                self.bucket[key_hash].remove(key)
        

    def contains(self, key: int) -> bool:
        key_hash = self.hash_func(key)
        if key in self.bucket[key_hash]:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)