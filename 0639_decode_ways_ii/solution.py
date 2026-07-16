# LeetCode 0639 - Decode Ways II
# https://leetcode.com/problems/decode-ways-ii/


class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10**9 + 7

        def one(ch: str) -> int:
            if ch == "*":
                return 9
            if ch == "0":
                return 0
            return 1

        def two(a: str, b: str) -> int:
            if a == "*" and b == "*":
                return 15
            if a == "*":
                return 2 if b <= "6" else 1
            if b == "*":
                if a == "1":
                    return 9
                if a == "2":
                    return 6
                return 0
            value = int(a) * 10 + int(b)
            return 1 if 10 <= value <= 26 else 0

        prev2, prev1 = 1, one(s[0])
        for i in range(1, len(s)):
            cur = (one(s[i]) * prev1 + two(s[i - 1], s[i]) * prev2) % mod
            prev2, prev1 = prev1, cur
        return prev1
