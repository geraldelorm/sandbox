class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]: 
        hashmap = {}
        commons = defaultdict(list)
        
        for i, v in enumerate(list1):
            hashmap[v] = i
            
        for i, v in enumerate(list2):
            if v in hashmap:
                commons[i+hashmap[v]].append(v)

        minIndexSum = min(commons.keys())
        return commons[minIndexSum]
        

# TC: O(n)
# SC: O(n)