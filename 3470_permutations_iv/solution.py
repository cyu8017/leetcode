# LeetCode 3470 - Permutations IV
# https://leetcode.com/problems/permutations-iv/

from typing import List


class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        fact = [0] * (n + 1)
        fact[0] = 1
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i
            if fact[i] > 10**18:
                fact[i] = 10**18 + 1
        used = [False] * (n + 1)
        ans: List[int] = []
        kk = k

        def dfs(pos: int) -> bool:
            nonlocal kk
            if pos == n:
                return True
            for x in range(1, n + 1):
                if used[x]:
                    continue
                if pos > 0 and (ans[pos - 1] % 2 == x % 2):
                    continue
                rem = n - pos - 1
                cnt = fact[rem]
                if cnt >= kk:
                    used[x] = True
                    ans.append(x)
                    if dfs(pos + 1):
                        return True
                    ans.pop()
                    used[x] = False
                else:
                    kk -= cnt
            return False

        if not dfs(0):
            return []
        return ans
