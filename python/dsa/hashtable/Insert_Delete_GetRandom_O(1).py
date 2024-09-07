class RandomizedSet:

    def __init__(self):
        self.bucket = {}
        self.items_list = []


    def insert(self, val: int) -> bool: #O(1)
        if val in self.bucket:
            return False
        self.bucket[val] = len(self.items_list)
        self.items_list.append(val)
        return True
        

    def remove(self, val: int) -> bool: #O(1)
        if val in self.bucket:
            val_index = self.bucket[val]
            last_item = self.items_list[-1]
            self.items_list[val_index], self.items_list[-1] = self.items_list[-1], self.items_list[val_index]
            self.bucket[last_item] = val_index
            self.items_list.pop()
            del self.bucket[val]

            return True
        return False
        

    def getRandom(self) -> int: #O(1)  
        return random.choice(self.items_list)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()