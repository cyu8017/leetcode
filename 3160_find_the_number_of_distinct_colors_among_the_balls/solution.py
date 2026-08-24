# LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        g = {}
        cnt = {}
        ans = [0] * len(queries)
        ai = 0
        for q in queries:
            x, y = q[0], q[1]
            cnt[y] = cnt.get(y, 0) + 1
            old = g.get(x)
            if old is not None:
                nv = cnt[old] - 1
                if nv == 0:
                    del cnt[old]
                else:
                    cnt[old] = nv
            g[x] = y
            ans[ai] = len(cnt)
            ai += 1
        return ans
