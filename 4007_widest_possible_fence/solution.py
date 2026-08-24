# LeetCode 4007 - Widest Possible Fence
# https://leetcode.com/problems/widest-possible-fence/

from typing import List


class Solution:
    def maximumWidth(self, planks: List[int]) -> int:
        cnt = {}
        for x in planks:
            cnt[x] = cnt.get(x, 0) + 1
        t = {}
        ans = 0
        for x, v1 in cnt.items():
            t[x] = t.get(x, 0) + v1
            ans = max(ans, t[x])
            t[x * 2] = t.get(x * 2, 0) + v1 // 2
            ans = max(ans, t[x * 2])
            for y, v2 in cnt.items():
                if y > x:
                    key = x + y
                    t[key] = t.get(key, 0) + min(v1, v2)
                    ans = max(ans, t[key])
        return ans
