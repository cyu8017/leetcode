# LeetCode 3003 - Maximize the Number of Partitions After Operations
# https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/


def popcount(x: int) -> int:
    c = 0
    while x != 0:
        c += x & 1
        x >>= 1
    return c


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        memo = {}

        def key(i: int, cur: int, t: int) -> int:
            return (i << 32) | (cur << 1) | t

        def dfs(i: int, cur: int, t: int) -> int:
            if i >= n:
                return 1
            kkey = key(i, cur, t)
            if kkey in memo:
                return memo[kkey]
            v = 1 << (ord(s[i]) - 97)
            nxt = cur | v
            if popcount(nxt) > k:
                ans = dfs(i + 1, v, t) + 1
            else:
                ans = dfs(i + 1, nxt, t)
            if t > 0:
                for j in range(26):
                    nxt = cur | (1 << j)
                    if popcount(nxt) > k:
                        ans = max(ans, dfs(i + 1, 1 << j, 0) + 1)
                    else:
                        ans = max(ans, dfs(i + 1, nxt, 0))
            memo[kkey] = ans
            return ans

        return dfs(0, 0, 1)
