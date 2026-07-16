# LeetCode 0944 - Delete Columns to Make Sorted
# https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        return sum(
            any(strs[r][c] > strs[r + 1][c] for r in range(len(strs) - 1))
            for c in range(len(strs[0]))
        )
