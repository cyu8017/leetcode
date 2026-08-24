# LeetCode 2106 - Maximum Fruits Harvested After at Most K Steps
# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        def min_steps(left: int, right: int, start: int) -> int:
            if right <= start:
                return start - left
            if left >= start:
                return right - start
            return min((start - left) + (right - left), (right - start) + (right - left))

        n = len(fruits)
        pref = [0] * (n + 1)
        pos = [0] * n
        for i, (p, amt) in enumerate(fruits):
            pos[i] = p
            pref[i + 1] = pref[i] + amt
        ans = 0
        j = 0
        for i in range(n):
            while j < n and min_steps(pos[i], pos[j], startPos) > k:
                j += 1
            if j <= i:
                ans = max(ans, pref[i + 1] - pref[j])
        j = 0
        for i in range(n):
            while j <= i and min_steps(pos[j], pos[i], startPos) > k:
                j += 1
            ans = max(ans, pref[i + 1] - pref[j])
        return ans
