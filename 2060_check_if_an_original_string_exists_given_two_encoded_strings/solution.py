# LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
# https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        memo = {}

        def is_digit(c: str) -> bool:
            return "0" <= c <= "9"

        def dfs(i: int, j: int, diff: int) -> bool:
            key = (i, j, diff)
            if key in memo:
                return memo[key]
            n, m = len(s1), len(s2)
            if i == n and j == m:
                memo[key] = diff == 0
                return diff == 0
            res = False
            if diff == 0 and i < n and j < m and not is_digit(s1[i]) and not is_digit(s2[j]):
                if s1[i] == s2[j]:
                    res = dfs(i + 1, j + 1, 0)
            elif diff > 0 and i < n and not is_digit(s1[i]):
                res = dfs(i + 1, j, diff - 1)
            elif diff < 0 and j < m and not is_digit(s2[j]):
                res = dfs(i, j + 1, diff + 1)
            if not res and i < n and is_digit(s1[i]):
                val = 0
                p = i
                while p < n and is_digit(s1[p]):
                    val = val * 10 + (ord(s1[p]) - 48)
                    if dfs(p + 1, j, diff + val):
                        res = True
                        break
                    p += 1
            if not res and j < m and is_digit(s2[j]):
                val = 0
                p = j
                while p < m and is_digit(s2[p]):
                    val = val * 10 + (ord(s2[p]) - 48)
                    if dfs(i, p + 1, diff - val):
                        res = True
                        break
                    p += 1
            memo[key] = res
            return res

        return dfs(0, 0, 0)
