# LeetCode 0942 - DI String Match
# https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        lo, hi = 0, len(s)
        ans = []
        for ch in s:
            if ch == "I":
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1
        ans.append(lo)
        return ans
