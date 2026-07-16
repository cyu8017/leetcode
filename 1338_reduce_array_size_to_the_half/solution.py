# LeetCode 1338 - Reduce Array Size To The Half

from collections import Counter
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        removed = 0
        for count, frequency in enumerate(sorted(Counter(arr).values(), reverse=True), 1):
            removed += frequency
            if removed * 2 >= len(arr):
                return count
        return 0
