from typing import List, Optional

from bisect import bisect_right

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        full, dry = {}, []
        for i, lake in enumerate(rains):
            if lake == 0:
                dry.append(i); ans[i] = 1
            else:
                if lake in full:
                    j = bisect_right(dry, full[lake])
                    if j == len(dry):
                        return []
                    ans[dry.pop(j)] = lake
                full[lake] = i
        return ans
