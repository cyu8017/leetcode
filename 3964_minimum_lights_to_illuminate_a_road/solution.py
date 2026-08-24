# LeetCode 3964 - Minimum Lights To Illuminate A Road
# https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/

from typing import List


class Solution:
    def minLights(self, lights: List[int]) -> int:
        n = len(lights)
        d = [0] * n
        for i in range(n):
            v = lights[i]
            if v > 0:
                l = max(0, i - v)
                r = min(n - 1, i + v)
                d[l] += 1
                if r + 1 < n:
                    d[r + 1] -= 1
        s = 0
        cnt = 0
        ans = 0
        for x in d:
            s += x
            if s == 0:
                cnt += 1
            else:
                ans += (cnt + 2) // 3
                cnt = 0
        ans += (cnt + 2) // 3
        return ans
