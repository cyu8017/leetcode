# LeetCode 0967 - Numbers With Same Consecutive Differences
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        ans: list[int] = []

        def dfs(num: int, length: int) -> None:
            if length == n:
                ans.append(num)
                return
            last = num % 10
            for nxt in {last + k, last - k}:
                if 0 <= nxt <= 9:
                    dfs(num * 10 + nxt, length + 1)

        for start in range(1, 10):
            dfs(start, 1)
        return ans
