# LeetCode 3889 - Mirror Frequency Distance
# https://leetcode.com/problems/mirror-frequency-distance/

from typing import Dict


class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq: Dict[str, int] = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        ans = 0
        vis: Dict[str, bool] = {}
        for c, v in freq.items():
            if "a" <= c <= "z":
                m = chr(97 + 25 - (ord(c) - 97))
            else:
                m = chr(48 + (9 - (ord(c) - 48)))
            if vis.get(m) is True:
                continue
            vis[c] = True
            mv = freq.get(m, 0)
            ans += abs(v - mv)
        return ans
