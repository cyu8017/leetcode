# LeetCode 2615 - Sum of Distances
# https://leetcode.com/problems/sum-of-distances/

from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pos = {}
        for i, x in enumerate(nums):
            if x not in pos:
                pos[x] = []
            pos[x].append(i)
        for idxs in pos.values():
            m = len(idxs)
            pref = [0] * (m + 1)
            for i in range(m):
                pref[i + 1] = pref[i] + idxs[i]
            for j in range(m):
                idx = idxs[j]
                left = j * idx - pref[j]
                right = pref[m] - pref[j + 1] - (m - 1 - j) * idx
                ans[idx] = left + right
        return ans
