from typing import List, Optional

from collections import Counter

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = Counter(x % k for x in arr)
        if count[0] % 2:
            return False
        return all(count[r] == count[k-r] for r in range(1, k))
