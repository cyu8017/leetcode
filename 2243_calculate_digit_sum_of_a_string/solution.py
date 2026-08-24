# LeetCode 2243 - Calculate Digit Sum of a String
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            nxt = []
            for i in range(0, len(s), k):
                total = 0
                end = min(i + k, len(s))
                for j in range(i, end):
                    total += ord(s[j]) - 48
                nxt.append(str(total))
            s = "".join(nxt)
        return s
