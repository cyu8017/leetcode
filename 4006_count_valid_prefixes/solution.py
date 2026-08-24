# LeetCode 4006 - Count Valid Prefixes
# https://leetcode.com/problems/count-valid-prefixes/


class Solution:
    def countValidPrefixes(self, s: str) -> int:
        ans = 0
        t = 0
        for i in range(len(s)):
            if s[i] == "1":
                t += 1
            else:
                t -= 1
            if t >= -1 and t <= 1:
                ans += 1
        return ans
