# LeetCode 2843 - Count Symmetric Integers
# https://leetcode.com/problems/count-symmetric-integers/


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for x in range(low, high + 1):
            s = str(x)
            if len(s) % 2 != 0:
                continue
            mid = len(s) // 2
            a = b = 0
            for i in range(mid):
                a += ord(s[i]) - 48
                b += ord(s[mid + i]) - 48
            if a == b:
                ans += 1
        return ans
