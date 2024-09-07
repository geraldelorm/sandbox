class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            
        seen, head, tail, longest_sub = set(), 0, 0, 0
        
        while tail < len(s):
            while s[tail] in seen and head < tail:
                seen.remove(s[head])
                head += 1
            longest_sub = max(longest_sub, (tail - head) + 1)
            seen.add(s[tail])
            tail += 1
        
        return longest_sub
        
        
# TC: O(n)
# SC: O(n)