# LeetCode 0959 - Regions Cut By Slashes
# https://leetcode.com/problems/regions-cut-by-slashes/

class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        parent = list(range(n * n * 4))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            parent[find(a)] = find(b)

        for r in range(n):
            for c in range(n):
                root = 4 * (r * n + c)
                ch = grid[r][c]
                if ch == "/":
                    union(root + 0, root + 3)
                    union(root + 1, root + 2)
                elif ch == "\\":
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)
                else:
                    union(root + 0, root + 1)
                    union(root + 1, root + 2)
                    union(root + 2, root + 3)
                if r + 1 < n:
                    union(root + 2, root + 4 * n + 0)
                if c + 1 < n:
                    union(root + 1, root + 4 + 3)

        return sum(find(i) == i for i in range(n * n * 4))
