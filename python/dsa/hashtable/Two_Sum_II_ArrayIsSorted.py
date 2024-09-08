class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		left, right = 0, len(numbers) - 1 #l = 0 r= 1

		while left < right:
			sum = numbers[left] + numbers[right] #9
			if sum > target:
				right -= 1
			elif sum < target:
				left += 1
			else:
				return [left +1, right +1] #[1, 2]
		return []


# TC: O(n)
# SC: O(1)
