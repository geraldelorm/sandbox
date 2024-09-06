class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup = {}
        
        for c in s:
            lookup[c] = lookup.get(c, 0) + 1
            
        for i, c in enumerate(s):
            if lookup[c] == 1:
                return i

        return -1
        
# TC: O(n)
# SC: O(n)