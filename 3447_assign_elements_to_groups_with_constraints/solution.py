# LeetCode 3447 - Assign Elements to Groups with Constraints
# https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

from typing import List


class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        max_v = 100001
        first = [-1] * max_v
        for i, e in enumerate(elements):
            if e < max_v and first[e] == -1:
                first[e] = i
        ans = [0] * len(groups)
        for gi, g in enumerate(groups):
            best = -1
            d = 1
            while d * d <= g:
                if g % d == 0:
                    if first[d] != -1 and (best == -1 or first[d] < best):
                        best = first[d]
                    other = g // d
                    if first[other] != -1 and (best == -1 or first[other] < best):
                        best = first[other]
                d += 1
            ans[gi] = best
        return ans
