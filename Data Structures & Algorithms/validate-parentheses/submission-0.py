from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        match = {"[":"]", "(":")","{":"}"}

        for c in s:
            if c in ["{","(","["]:
                stack.append(c)
                continue 
            elif not stack or c != match[stack.pop()]:
                return False
        
        return len(stack) == 0