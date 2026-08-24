# LeetCode 2391 - Minimum Amount of Time to Collect Garbage
# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        last_m = last_p = last_g = 0
        for i, g in enumerate(garbage):
            ans += len(g)
            for c in g:
                if c == "M":
                    last_m = i
                elif c == "P":
                    last_p = i
                else:
                    last_g = i
        pref = [0] * (len(travel) + 1)
        for i in range(len(travel)):
            pref[i + 1] = pref[i] + travel[i]
        ans += pref[last_m] + pref[last_p] + pref[last_g]
        return ans
