# LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
# https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

from typing import List


class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
        freq = {0: 1}
        ans = 0

        def dfs(u: int, mask: int) -> None:
            nonlocal ans
            for v in g[u]:
                nm = mask ^ (1 << (ord(s[v]) - 97))
                ans += freq.get(nm, 0)
                for b in range(26):
                    ans += freq.get(nm ^ (1 << b), 0)
                freq[nm] = freq.get(nm, 0) + 1
                dfs(v, nm)

        dfs(0, 0)
        return ans
