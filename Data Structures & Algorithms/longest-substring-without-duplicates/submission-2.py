class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        chars=collections.deque([])
        res = 1
        for c in s:
            if c in chars:
                res = max(len(chars), res)
                while chars.popleft() != c:
                    continue
            
            chars.append(c)
        
        return max(len(chars), res)
