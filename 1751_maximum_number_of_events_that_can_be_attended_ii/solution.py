import bisect
from functools import lru_cache

class Solution:
    def maxValue(self, events, k):
        events = sorted(events)
        n = len(events)
        starts = [e[0] for e in events]

        @lru_cache(None)
        def dp(i, remain):
            if i >= n or remain == 0:
                return 0
            skip = dp(i + 1, remain)
            j = bisect.bisect_right(starts, events[i][1])
            take = events[i][2] + dp(j, remain - 1)
            return max(skip, take)

        return dp(0, k)
