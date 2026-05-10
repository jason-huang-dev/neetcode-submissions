def get_hash(word: str)->tuple:
    chars = [0]*26
    for c in word:
        chars[ord(c) - ord("a")] += 1
    return tuple(chars)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for word in strs:
            curr_group = get_hash(word)
            if curr_group in groups:
                groups[curr_group].append(word)
            else:
                groups[curr_group] = [word]
        
        return [value for value in groups.values()]