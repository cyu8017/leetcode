# LeetCode 2938 - Separate Black and White Balls
# https://leetcode.com/problems/separate-black-and-white-balls/


class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        zeros = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                zeros += 1
            else:
                ans += zeros
        return ans
