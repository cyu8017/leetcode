# LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
# https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/


class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        m = len(initial)
        n = len(target)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        mx = 0
        for i in range(m):
            for j in range(n):
                if initial[i] == target[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
                    mx = max(mx, f[i + 1][j + 1])
        return m + n - 2 * mx
