from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return sum(value for value, count in counts.items() if count == 1)
