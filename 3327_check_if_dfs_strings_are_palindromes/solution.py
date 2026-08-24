# LeetCode 3327 - Check DFS Strings Are Palindromes
# https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

from typing import List


class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
        ans = [False] * n

        def isPal(t: str) -> bool:
            i, j = 0, len(t) - 1
            while i < j:
                if t[i] != t[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfsStr(u: int) -> str:
            out = ""
            for v in g[u]:
                out += dfsStr(v)
            out += s[u]
            ans[u] = isPal(out)
            return out

        dfsStr(0)
        return ans
