# LeetCode 2048 - Next Greater Numerically Balanced Number
# https://leetcode.com/problems/next-greater-numerically-balanced-number/


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def balanced(x: int) -> bool:
            cnt = [0] * 10
            while x > 0:
                cnt[x % 10] += 1
                x //= 10
            for d in range(10):
                if cnt[d] != 0 and cnt[d] != d:
                    return False
            return True

        x = n + 1
        while True:
            if balanced(x):
                return x
            x += 1
