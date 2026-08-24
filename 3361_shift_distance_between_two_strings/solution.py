# LeetCode 3361 - Shift Distance Between Two Strings
# https://leetcode.com/problems/shift-distance-between-two-strings/

from typing import List


class Solution:
    def shiftDistance(
        self, s: str, t: str, nextCost: List[int], previousCost: List[int]
    ) -> int:
        ans = 0
        for i in range(len(s)):
            a = ord(s[i]) - 97
            b = ord(t[i]) - 97
            if a == b:
                continue
            fwd = 0
            x = a
            while x != b:
                fwd += nextCost[x]
                x = (x + 1) % 26
            bwd = 0
            x = a
            while x != b:
                bwd += previousCost[x]
                x = (x + 25) % 26
            ans += fwd if fwd < bwd else bwd
        return ans
