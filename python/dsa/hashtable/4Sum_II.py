# class Solution:
#     def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
#         count = 0
        
#         for value1 in nums1:
#             for value2 in nums2:
#                 for value3 in nums3:
#                     for value4 in nums4:
#                         if value1 + value2 + value3 + value4 == 0:
#                             count += 1
#         return count

# # TC: O(n^4)
# # SC: O(1)

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap, count = defaultdict(int), 0
        
        for value1 in nums1:
            for value2 in nums2:
                sum = value1 + value2
                hashmap[sum] += 1
                
                
        for value3 in nums3:
            for value4 in nums4:
                sum = value3 + value4
                compliment = sum * -1
                
                if compliment in hashmap:
                    count += hashmap[compliment]

        return count

# TC: O(n^2)
# SC: O(n^2)