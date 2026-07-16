# LeetCode 1513

class Solution:
    def numSub(self, s):
        ans = run = 0
        for ch in s:
            run = run + 1 if ch == "1" else 0
            ans += run
        return ans % 1000000007
