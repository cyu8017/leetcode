# LeetCode 0440 - K-th Smallest in Lexicographical Order
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1

        while k > 0:
            steps = self._count_steps(n, current, current + 1)
            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1

        return current

    def _count_steps(self, n: int, first: int, last: int) -> int:
        steps = 0
        while first <= n:
            steps += min(n + 1, last) - first
            first *= 10
            last *= 10
        return steps
