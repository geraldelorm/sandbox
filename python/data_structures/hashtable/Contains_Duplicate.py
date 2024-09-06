# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for i in range(0, len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
        
#         return False

#TC = O(n^2)
#SC = O(1)

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i -1] == nums[i]:
#                     return True     
#         return False

#TC = O(nlogn)
#SC = O(1)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for ele in nums:
            if ele in hashset:
                return True 
            hashset.add(ele)
        return False

#TC = O(n)
#SC = O(n)