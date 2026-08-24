# LeetCode 2180 - Count Integers With Even Digit Sum
# https://leetcode.com/problems/count-integers-with-even-digit-sum/
class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for x in range(1, (num) + 1):
            s = 0
            y = x
            while y > 0:
                s += y % 10
                y = y // 10
            if s % 2 == 0:
                ans += 1
        return ans
