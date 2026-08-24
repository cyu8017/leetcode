# LeetCode 2992 - Number of Self-Divisible Permutations
# https://leetcode.com/problems/number-of-self-divisible-permutations/


def gcd(a: int, b: int) -> int:
    while b != 0:
        t = a % b
        a = b
        b = t
    return a


class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        ans = 0
        used = [False] * (n + 1)

        def dfs(pos: int) -> None:
            nonlocal ans
            if pos > n:
                ans += 1
                return
            for v in range(1, n + 1):
                if used[v]:
                    continue
                if gcd(v, pos) != 1:
                    continue
                used[v] = True
                dfs(pos + 1)
                used[v] = False

        dfs(1)
        return ans
