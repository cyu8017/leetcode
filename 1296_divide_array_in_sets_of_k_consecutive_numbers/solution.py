from collections import Counter
from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        counts = Counter(nums)
        for start in sorted(counts):
            amount = counts[start]
            if amount:
                for value in range(start, start + k):
                    if counts[value] < amount:
                        return False
                    counts[value] -= amount
        return True
