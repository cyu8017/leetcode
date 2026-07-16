# LeetCode 0955 - Delete Columns to Make Sorted II
# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n, m = len(strs), len(strs[0])
        sorted_pair = [False] * (n - 1)
        deleted = 0
        for c in range(m):
            if any(
                not sorted_pair[r] and strs[r][c] > strs[r + 1][c]
                for r in range(n - 1)
            ):
                deleted += 1
                continue
            for r in range(n - 1):
                if strs[r][c] < strs[r + 1][c]:
                    sorted_pair[r] = True
        return deleted
