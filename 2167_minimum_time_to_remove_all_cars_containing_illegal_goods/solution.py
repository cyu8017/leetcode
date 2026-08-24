# LeetCode 2167 - Minimum Time to Remove All Cars Containing Illegal Goods
# https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/
class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        left = [0] * (n)
        if s[0] == "1":
            left[0] = 1
        for i in range(1, n):
            left[i] = left[i - 1]
            if s[i] == "1":
                left[i] = min(i + 1, left[i - 1] + 2)
        ans = left[n - 1]
        right = 0
        for i in range(n - 1, (0) - 1, -1):
            if s[i] == "1":
                right = min(n - i, right + 2)
            leftCost = left[i - 1] if i > 0 else 0
            ans = min(ans, leftCost + right)
        return ans
