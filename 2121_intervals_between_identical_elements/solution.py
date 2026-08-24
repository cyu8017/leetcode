# LeetCode 2121 - Intervals Between Identical Elements
# https://leetcode.com/problems/intervals-between-identical-elements/

from typing import List
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        pos = {}
        for i in range(n):
            if arr[i] not in pos:
                pos[arr[i]] = []
            pos.get(arr[i]).append(i)
        ans = [0] * (n)
        for idxs in list(pos.values()):
            m = len(idxs)
            pref = [0] * (m + 1)
            for i in range(m):
                pref[i + 1] = pref[i] + idxs[i]
            for i in range(m):
                left = i * idxs[i] - pref[i]
                right = (pref[m] - pref[i + 1]) - (m - i - 1) * idxs[i]
                ans[idxs[i]] = left + right
        return ans
