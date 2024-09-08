class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        def twoSum(start):
            left, right = start + 1, len(nums) - 1
            while left < right:
                sum = nums[start] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append((nums[start], nums[left], nums[right]))
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            twoSum(i)
                
        return result


# TC : O(N^2)
# SC: O(1) #depends on the stackmand recursion could be O(n)