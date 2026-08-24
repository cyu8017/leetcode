# LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

from typing import List


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        m = len(conflictingPairs)
        best = 0
        for skip in range(m):
            right_limit = [n + 1] * (n + 2)
            for i in range(m):
                if i == skip:
                    continue
                a, b = conflictingPairs[i][0], conflictingPairs[i][1]
                if a > b:
                    a, b = b, a
                if b < right_limit[a]:
                    right_limit[a] = b
            min_right = n + 1
            cnt = 0
            for l in range(n, 0, -1):
                if right_limit[l] < min_right:
                    min_right = right_limit[l]
                cnt += min_right - l
            if cnt > best:
                best = cnt
        return best
