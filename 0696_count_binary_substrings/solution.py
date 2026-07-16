# LeetCode 0696 - Count Binary Substrings
# https://leetcode.com/problems/count-binary-substrings/


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        cur = 1
        ans = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                ans += min(prev, cur)
                prev = cur
                cur = 1
        return ans + min(prev, cur)
