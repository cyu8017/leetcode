# LeetCode 3228 - Maximum Number of Operations to Move Ones to the End
# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

class Solution:
    def maxOperations(self, s: str) -> int:
        ans, cnt = 0, 0
        for i in range(len(s)):
            if s[i] == "1":
                cnt += 1
            elif i > 0 and s[i - 1] == "1":
                ans += cnt
        return ans
