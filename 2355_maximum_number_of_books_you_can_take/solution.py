# LeetCode 2355 - Maximum Number of Books You Can Take
# https://leetcode.com/problems/maximum-number-of-books-you-can-take/

from typing import List


class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        dp = [0] * n
        stack = []

        def interval_sum(l: int, r: int, h: int) -> int:
            width = r - l + 1
            if h >= width:
                return width * (2 * h - width + 1) // 2
            return h * (h + 1) // 2

        ans = 0
        for i in range(n):
            while stack and books[stack[-1]] >= books[i] - (i - stack[-1]):
                stack.pop()
            if not stack:
                dp[i] = interval_sum(0, i, books[i])
            else:
                j = stack[-1]
                dp[i] = dp[j] + interval_sum(j + 1, i, books[i])
            ans = max(ans, dp[i])
            stack.append(i)
        return ans
