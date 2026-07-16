from typing import List, Optional

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        prereq = [0] * n
        for a, b in relations:
            prereq[b-1] |= 1 << (a-1)
        full, inf = (1 << n) - 1, 10**9
        dp = [inf] * (1 << n); dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] == inf:
                continue
            available = 0
            for c in range(n):
                if not mask >> c & 1 and prereq[c] & mask == prereq[c]:
                    available |= 1 << c
            choices = [available] if available.bit_count() <= k else []
            if not choices:
                sub = available
                while sub:
                    if sub.bit_count() == k:
                        choices.append(sub)
                    sub = (sub - 1) & available
            for take in choices:
                dp[mask | take] = min(dp[mask | take], dp[mask] + 1)
        return dp[full]
