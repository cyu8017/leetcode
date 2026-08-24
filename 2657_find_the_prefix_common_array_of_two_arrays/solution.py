# LeetCode 2657 - Find the Prefix Common Array of Two Arrays
# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen_a = [False] * (n + 1)
        seen_b = [False] * (n + 1)
        ans = [0] * n
        common = 0
        for i in range(n):
            if seen_b[A[i]]:
                common += 1
            seen_a[A[i]] = True
            if seen_a[B[i]]:
                common += 1
            seen_b[B[i]] = True
            ans[i] = common
        return ans
