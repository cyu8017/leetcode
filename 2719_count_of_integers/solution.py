# LeetCode 2719 - Count of Integers
# https://leetcode.com/problems/count-of-integers/


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 1000000007

        def dec(s: str) -> str:
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == "0":
                arr[i] = "9"
                i -= 1
            if i >= 0:
                arr[i] = chr(ord(arr[i]) - 1)
            j = 0
            while j < len(arr) - 1 and arr[j] == "0":
                j += 1
            return "".join(arr[j:])

        def dp(s: str) -> int:
            memo = {}

            def dfs(pos: int, sm: int, tight: bool) -> int:
                if sm > max_sum:
                    return 0
                if pos == len(s):
                    return 1 if sm >= min_sum else 0
                key = (pos, sm, tight)
                if key in memo:
                    return memo[key]
                up = ord(s[pos]) - 48 if tight else 9
                res = 0
                for d in range(up + 1):
                    res = (res + dfs(pos + 1, sm + d, tight and d == up)) % MOD
                memo[key] = res
                return res

            return dfs(0, 0, True)

        return (dp(num2) - dp(dec(num1)) + MOD) % MOD
