# LeetCode 0351 - Android Unlock Patterns
# https://leetcode.com/problems/android-unlock-patterns/


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        jumps = {
            (0, 2): 1,
            (2, 0): 1,
            (0, 6): 3,
            (6, 0): 3,
            (0, 8): 4,
            (8, 0): 4,
            (2, 8): 5,
            (8, 2): 5,
            (2, 6): 7,
            (6, 2): 7,
            (6, 8): 7,
            (8, 6): 7,
            (1, 7): 8,
            (7, 1): 8,
            (3, 7): 6,
            (7, 3): 6,
            (1, 5): 4,
            (5, 1): 4,
            (3, 5): 5,
            (5, 3): 5,
            (1, 3): 2,
            (3, 1): 2,
            (4, 5): 5,
            (5, 4): 5,
            (4, 7): 8,
            (7, 4): 8,
            (4, 3): 5,
            (3, 4): 5,
            (4, 1): 2,
            (1, 4): 2,
            (4, 6): 7,
            (6, 4): 7,
            (4, 8): 6,
            (8, 4): 6,
            (4, 0): 2,
            (0, 4): 2,
            (4, 2): 6,
            (2, 4): 6,
        }

        def is_valid(visited: int, last: int, next_cell: int) -> bool:
            if visited & (1 << next_cell):
                return False
            if (last, next_cell) in jumps:
                return not (visited & (1 << jumps[(last, next_cell)]))
            return (
                abs(last // 3 - next_cell // 3) <= 1
                and abs(last % 3 - next_cell % 3) <= 1
            )

        def dfs(visited: int, last: int, length: int) -> int:
            if length > n:
                return 0

            count = 1 if m <= length <= n else 0
            for next_cell in range(9):
                if is_valid(visited, last, next_cell):
                    count += dfs(visited | (1 << next_cell), next_cell, length + 1)
            return count

        return (
            dfs(1 << 0, 0, 1) * 4
            + dfs(1 << 1, 1, 1) * 4
            + dfs(1 << 4, 4, 1)
        )
