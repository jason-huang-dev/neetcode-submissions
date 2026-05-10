class Solution:
    """
    Understand:
        Can I assume that the input is List[int] or None?
        In the case that we have happy case [1,1,1,2,2,2] this should return True correct? As we can see that either 1 or 2 has duplicates.
        In the edge case of [x] just one element this will always be False?
        In the average case of [1,2,2,3] this would return True due to 2 having duplicates?
    Match:
        Two Pointers: ❌ Not helpful here since we're not working with sorted input or looking for a specific pair/sum — good call.
        Sliding Window: ❌ Right again — sliding window helps with contiguous subarrays, which isn’t necessary when any two elements in the array can be duplicates.
        Hash Set / One Pass: ✅ Perfect match. Constant time lookup, and early exit as soon as we find a duplicate — efficient and clean.
    Plan:
        If nums is None or empty, return False.
        Initialize an empty set called seen.
        For each number in nums:
        If it's already in seen, return True.
        Otherwise, add it to seen.
        If the loop finishes, return False.
    Implement:
    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        seen = set();
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    """
    Review:

    Explain:
    """
         