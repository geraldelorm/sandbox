#Brute force 
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result, seen_quadruplets = [], set()
        
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                for c in range(b + 1, len(nums)):
                    for d in range(c + 1, len(nums)):
                        sum = nums[a] + nums[b] + nums[c] + nums[d]
                        if sum == target and (nums[a], nums[b], nums[c], nums[d]) not in seen_quadruplets:
                            result.append([nums[a], nums[b], nums[c], nums[d]])
                            seen_quadruplets.add((nums[a], nums[b], nums[c], nums[d]))
                            
        return result


# TC: O(n^4)
# SC: O(n)


#Brute force 
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        
        def twoSum(start, i):
            left, right = start + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[start] + nums[left] + nums[right]
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    result.append((nums[i], nums[start], nums[left], nums[right]))
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue          
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                twoSum(j, i)
                
        return result


# TC: O(n^3)
# SC: O(n)