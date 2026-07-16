# LeetCode 0960 - Delete Columns to Make Sorted III
# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        m = len(strs[0])
        dp = [1] * m
        for j in range(m):
            for i in range(j):
                if all(row[i] <= row[j] for row in strs):
                    dp[j] = max(dp[j], dp[i] + 1)
        return m - max(dp)
