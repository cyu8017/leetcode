from collections import Counter
from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = 10 ** 9 + 7
        seen = Counter()
        ans = 0
        for value in deliciousness:
            for power in range(22):
                ans += seen[(1 << power) - value]
            seen[value] += 1
        return ans % mod
