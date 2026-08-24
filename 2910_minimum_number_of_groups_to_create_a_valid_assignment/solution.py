# LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
# https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

from typing import List


class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        freq = {}
        for b in balls:
            freq[b] = freq.get(b, 0) + 1
        counts = list(freq.values())
        min_f = min(counts)
        for size in range(min_f, 0, -1):
            ok = True
            groups = 0
            for c in counts:
                rem = c % (size + 1)
                g2 = c // (size + 1)
                if rem == 0:
                    groups += g2
                elif size - rem <= g2:
                    groups += g2 + 1
                else:
                    ok = False
                    break
            if ok:
                return groups
        return len(balls)
