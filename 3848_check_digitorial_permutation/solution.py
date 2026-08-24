# LeetCode 3848 - Check Digitorial Permutation
# https://leetcode.com/problems/check-digitorial-permutation/


class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        f = [0] * 10
        f[0] = 1
        for i in range(1, 10):
            f[i] = f[i - 1] * i
        x = 0
        y = n
        while y > 0:
            x += f[y % 10]
            y //= 10
        a = "".join(sorted(str(x)))
        b = "".join(sorted(str(n)))
        return a == b
