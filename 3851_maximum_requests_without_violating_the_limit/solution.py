# LeetCode 3851 - Maximum Requests Without Violating The Limit
# https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

from typing import Dict, List


class Solution:
    def maxRequests(self, requests: List[List[int]], k: int, window: int) -> int:
        g: Dict[int, List[int]] = {}
        for r in requests:
            g.setdefault(r[0], []).append(r[1])
        ans = len(requests)
        for ts in g.values():
            ts.sort()
            kept: List[int] = []
            for t in ts:
                while kept and t - kept[0] > window:
                    kept.pop(0)
                if len(kept) < k:
                    kept.append(t)
                else:
                    ans -= 1
        return ans
