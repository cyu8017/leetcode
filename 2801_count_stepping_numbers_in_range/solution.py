# LeetCode 2801 - Count Stepping Numbers in Range
# https://leetcode.com/problems/count-stepping-numbers-in-range/


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
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

        def count_to(s: str) -> int:
            memo = [
                [[[-1] * 2 for _ in range(11)] for _ in range(2)] for _ in range(105)
            ]

            def dfs(pos: int, tight: int, last: int, started: int) -> int:
                if pos == len(s):
                    return started
                if memo[pos][tight][last + 1][started] != -1:
                    return memo[pos][tight][last + 1][started]
                up = ord(s[pos]) - 48 if tight else 9
                ans = 0
                for d in range(up + 1):
                    nt = 1 if tight and d == up else 0
                    if not started:
                        if d == 0:
                            ans += dfs(pos + 1, nt, -1, 0)
                        else:
                            ans += dfs(pos + 1, nt, d, 1)
                    elif abs(d - last) == 1:
                        ans += dfs(pos + 1, nt, d, 1)
                memo[pos][tight][last + 1][started] = ans % MOD
                return memo[pos][tight][last + 1][started]

            return dfs(0, 1, -1, 0)

        ans = (count_to(high) - count_to(dec(low))) % MOD
        if ans < 0:
            ans += MOD
        return ans
