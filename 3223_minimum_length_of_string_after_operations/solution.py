# LeetCode 3223 - Minimum Length of String After Operations
# https://leetcode.com/problems/minimum-length-of-string-after-operations/

class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1
        ans = 0
        for x in cnt:
            if x > 0:
                ans += 1 if (x & 1) != 0 else 2
        return ans
