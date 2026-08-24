# LeetCode 2747 - Count Zero Request Servers
# https://leetcode.com/problems/count-zero-request-servers/

from typing import List


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda e: e[1])
        qs = sorted(((t, i) for i, t in enumerate(queries)), key=lambda q: q[0])
        ans = [0] * len(queries)
        cnt = {}
        active, l, r = 0, 0, 0
        for t, qi in qs:
            while r < len(logs) and logs[r][1] <= t:
                sid = logs[r][0]
                c = cnt.get(sid, 0)
                if c == 0:
                    active += 1
                cnt[sid] = c + 1
                r += 1
            while l < r and logs[l][1] < t - x:
                sid = logs[l][0]
                c = cnt[sid] - 1
                cnt[sid] = c
                if c == 0:
                    active -= 1
                l += 1
            ans[qi] = n - active
        return ans
