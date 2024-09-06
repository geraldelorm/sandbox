class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        
        for ele in nums:
            if ele in hashmap:
                hashmap[ele] += 1
            else:
                hashmap[ele] = 1

        for ele in nums:
            if hashmap[ele] == 1:
                return ele

#TC: O(n)
#SC: O(n)

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         buffer = 0

#         for ele in nums:
#             buffer = buffer ^ ele

#         return buffer

# TC: O(n)
# SC: O(1)