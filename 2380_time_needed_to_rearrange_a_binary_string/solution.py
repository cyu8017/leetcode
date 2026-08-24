# LeetCode 2380 - Time Needed to Rearrange a Binary String
# https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = zeros = 0
        for c in s:
            if c == "0":
                zeros += 1
            elif zeros > 0:
                ans = max(ans + 1, zeros)
        return ans
