from collections import Counter
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counts = Counter()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                counts[nums[i] * nums[j]] += 1
        return sum(count * (count - 1) * 4 for count in counts.values())
