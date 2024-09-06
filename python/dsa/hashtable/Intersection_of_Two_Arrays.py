class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset = set(nums1)
        result = []

        for ele in nums2:
            if ele in hashset:
                result.append(ele)
                hashset.remove(ele)
                
        return result
        

# TC: O(n)
# SC: O(n)