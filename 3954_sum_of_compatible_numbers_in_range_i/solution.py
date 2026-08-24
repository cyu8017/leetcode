# LeetCode 3954 - Sum Of Compatible Numbers In Range I
# https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/


class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        start = max(1, n - k)
        end = n + k
        ans = 0
        for x in range(start, end + 1):
            if (n & x) == 0:
                ans += x
        return ans
