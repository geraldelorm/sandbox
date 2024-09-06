class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = {}
        
        for index, value in enumerate(nums):
            if value in lookup and abs(lookup[value] - index) <= k:
                return True
            lookup[value] = index
            
        return False
        

# TC: O(n)
# SC: O(n)