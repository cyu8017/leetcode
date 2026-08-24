# LeetCode 2165 - Smallest Value of the Rearranged Number
# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/
class Solution:
    def smallestNumber(self, num: int) -> int:
        neg = num < 0
        if neg:
            num = -num
        if num == 0:
            return 0
        digits = []
        while num > 0:
            digits.append(num % 10)
            num = num // 10
        if neg:
            digits.sort(reverse=True)
            ans = 0
            for d in digits:
                ans = ans * 10 + d
            return -ans
        digits.sort()
        if digits[0] == 0:
            for i in range(1, len(digits)):
                if digits[i] != 0:
                    t = digits[0]
                    digits[0] = digits[i]
                    digits[i] = t
                    break
        res = 0
        for d in digits:
            res = res * 10 + d
        return res
