# LeetCode 2315 - Count Asterisks
# https://leetcode.com/problems/count-asterisks/


class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        inside = False
        for c in s:
            if c == "|":
                inside = not inside
            elif c == "*" and not inside:
                ans += 1
        return ans
