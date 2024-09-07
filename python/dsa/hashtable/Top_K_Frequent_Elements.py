class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        
        sorted_freq = sorted(frequency.values(), reverse=True)
        
        result = []
        
        for i in range(k):
            for v in frequency:
                if frequency[v] == sorted_freq[i]:
                    result.append(v)
                    frequency[v] = None
                    
                    
        return result
            
# TC: O(nlogn)
# sc: O(n)
        