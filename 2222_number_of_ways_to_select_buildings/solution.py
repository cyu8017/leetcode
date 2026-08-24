# LeetCode 2222 - Number of Ways to Select Buildings
# https://leetcode.com/problems/number-of-ways-to-select-buildings/


class Solution:
    def numberOfWays(self, s: str) -> int:
        total0 = s.count("0")
        total1 = len(s) - total0
        left0 = left1 = ans = 0
        for c in s:
            if c == "0":
                ans += left1 * (total1 - left1)
                left0 += 1
            else:
                ans += left0 * (total0 - left0)
                left1 += 1
        return ans
