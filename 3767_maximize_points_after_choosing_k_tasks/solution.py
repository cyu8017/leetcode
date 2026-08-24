# LeetCode 3767 - Maximize Points After Choosing K Tasks
# https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

from typing import List


class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n = len(technique1)
        idx = list(range(n))
        idx.sort(key=lambda i: -(technique1[i] - technique2[i]))
        ans = sum(technique2)
        for i in range(k):
            index = idx[i]
            ans -= technique2[index]
            ans += technique1[index]
        for i in range(k, n):
            index = idx[i]
            if technique1[index] >= technique2[index]:
                ans -= technique2[index]
                ans += technique1[index]
        return ans
