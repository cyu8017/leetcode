# LeetCode 2607 - Make K-Subarray Sums Equal
# https://leetcode.com/problems/make-k-subarray-sums-equal/

from typing import List


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        n = len(arr)
        g = gcd(n, k)
        ans = 0
        for r in range(g):
            group = [arr[i] for i in range(r, n, g)]
            group.sort()
            med = group[len(group) // 2]
            for x in group:
                ans += abs(x - med)
        return ans
