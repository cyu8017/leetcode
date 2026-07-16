# LeetCode 0830 - Positions of Large Groups
# https://leetcode.com/problems/positions-of-large-groups/

class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        ans = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            if j - i >= 3:
                ans.append([i, j - 1])
            i = j
        return ans
