# LeetCode 0753 - Cracking the Safe
# https://leetcode.com/problems/cracking-the-safe/


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        seen: set[str] = set()
        path: list[str] = []
        start = "0" * (n - 1)

        def dfs(node: str) -> None:
            for digit in map(str, range(k)):
                edge = node + digit
                if edge not in seen:
                    seen.add(edge)
                    dfs(edge[1:])
                    path.append(digit)

        dfs(start)
        return "".join(path) + start
