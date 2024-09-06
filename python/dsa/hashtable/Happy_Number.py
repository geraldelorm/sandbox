class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        def getNewNum(n):
            newNum = 0
            
            while n > 0:
                digit = n % 10
                newNum += digit**2             
                n = n // 10
                
            return newNum
            
        while n > 1:
            n = getNewNum(n)
            if n in seen:
                return False
            seen.add(n)
            
        return True
        
# TC: O(logN)
# SC: O(k)