class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool: 
        s_map, t_map = {}, {} 

        for i in range(len(s)):
            s_val, t_val = s[i], t[i]
            
            if ((s_val in s_map and s_map[s_val] != t_val) 
                or (t_val in t_map and t_map[t_val] != s_val)):
                return False
            
            s_map[s_val] = t_val
            t_map[t_val] = s_val
            
        return True