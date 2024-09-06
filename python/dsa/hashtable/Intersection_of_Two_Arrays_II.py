class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup, output = {}, []
        
        for v in nums1:
            lookup[v] = lookup.get(v, 0) + 1 

        for v in nums2:
            if v in lookup:
                output.append(v)
                lookup[v] -= 1
                if lookup[v] == 0:
                    del lookup[v] 
                    
        return output

# TC: O(n)
# SC: O(n)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup, output = {}, []
        
        for v in nums1:
            lookup[v] = lookup.get(v, 0) + 1 

        for v in nums2:
            if v in lookup and lookup[v] > 0:
                output.append(v)
                lookup[v] -= 1
        return output

# TC: O(n)
# SC: O(n) 