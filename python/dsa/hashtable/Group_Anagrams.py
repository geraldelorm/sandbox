# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hashmap = defaultdict(list)
        
#         for string in strs:
#             key = str(sorted(string))
            
#             hashmap[key].append(string)
            
#         return list(hashmap.values())
        
# # TC: O(nmlogm)
# # SC: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getCharCount(string):
            charArray = [0] * 26
            for c in string:
                index = ord(c) - ord("a")
                charArray[index] += 1
                
            return tuple(charArray)
        
        hashmap = defaultdict(list)
        
        for string in strs:
            key = getCharCount(string)
            
            hashmap[key].append(string)
            
        return list(hashmap.values())

# tc: O(nm)
# sc: O(n)