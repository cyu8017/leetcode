# LeetCode 3448 - Count Substrings Divisible By Last Digit
# https://leetcode.com/problems/count-substrings-divisible-by-last-digit/


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for r in range(n):
            last = ord(s[r]) - 48
            if last == 0:
                continue
            mod = 0
            p = 1 % last
            for l in range(r, -1, -1):
                mod = (mod + (ord(s[l]) - 48) * p) % last
                p = (p * 10) % last
                if mod == 0:
                    ans += 1
        return ans
