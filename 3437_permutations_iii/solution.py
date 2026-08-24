# LeetCode 3437 - Permutations III
# https://leetcode.com/problems/permutations-iii/

from typing import List


class Solution:
    def permute(self, n: int) -> List[List[int]]:
        ans: List[List[int]] = []
        used = [False] * (n + 1)
        cur: List[int] = []

        def dfs() -> None:
            if len(cur) == n:
                ans.append(cur[:])
                return
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cur and (cur[-1] % 2 == i % 2):
                    continue
                used[i] = True
                cur.append(i)
                dfs()
                cur.pop()
                used[i] = False

        dfs()
        return ans
