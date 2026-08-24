# LeetCode 3773 - Maximum Number of Equal Length Runs
# https://leetcode.com/problems/maximum-number-of-equal-length-runs/

class Solution:
    def maxSameLengthRuns(self, s: str) -> int:
        cnt = {}
        n = len(s)
        ans = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            m = j - i
            cnt[m] = cnt.get(m, 0) + 1
            ans = max(ans, cnt[m])
            i = j
        return ans
