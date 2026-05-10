from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        chars = Counter(s)
        
        for char in t:
            if char in chars and chars[char] > 0:
                chars[char] -= 1
            else:
                return False
        
        return True
