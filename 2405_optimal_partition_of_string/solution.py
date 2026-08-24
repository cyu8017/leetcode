# LeetCode 2405 - Optimal Partition of String
# https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1
        seen = 0
        for c in s:
            bit = 1 << (ord(c) - 97)
            if (seen & bit) != 0:
                ans += 1
                seen = 0
            seen |= bit
        return ans
