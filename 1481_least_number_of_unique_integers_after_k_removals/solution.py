from typing import List, Optional

from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = sorted(Counter(arr).values())
        removed = 0
        for count in counts:
            if k < count:
                break
            k -= count; removed += 1
        return len(counts) - removed
