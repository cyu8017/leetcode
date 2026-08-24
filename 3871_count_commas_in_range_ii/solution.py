# LeetCode 3871 - Count Commas In Range II
# https://leetcode.com/problems/count-commas-in-range-ii/


class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        x = 1000
        while x <= n:
            ans += n - x + 1
            x *= 1000
        return ans
