# LeetCode 4000 - Largest Integer With Given Digit Sum
# https://leetcode.com/problems/largest-integer-with-given-digit-sum/


class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if n * 9 < s:
            return -1
        ans = 0
        for i in range(n):
            x = s if s < 9 else 9
            ans = ans * 10 + x
            s -= x
        return ans
