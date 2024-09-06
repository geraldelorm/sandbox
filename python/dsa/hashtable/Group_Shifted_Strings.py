Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

"abc" = 1, 1 => 0, 1, 2
"bcd" = 1, 1 => 1, 2, 3
"acef" = 2, 1, 1 => 0, 2, 4, 5
"xyz" = 1, 1 => 23, 24, 25
"az" = 1 => 0, 25
"ba" = 1 => 1, 0
"a" = 0 => 0
"z" = 0 => 25


from collections import defaultdict

class Solution:
    def groupShiftedString(self, strs: list) -> list:
        hashmap = defaultdict(list)

        for string in strs:
            key =  self.getKey(str)

            hashmap[key].append(string)

        return list(hashmap.values())
    
    def getKey(self, string):
        key = []
        for i in range(1, len(string)):
            diff = ord(string[i]) - ord(string[i-1])
            key.append(diff if diff >= 0 else diff + 26)
            
        return tuple(key)
