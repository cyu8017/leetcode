# LeetCode 3895 - Count Digit Appearances
# https://leetcode.com/problems/count-digit-appearances/

from typing import List


class Solution:
    def countDigitOccurrences(self, nums: List[int], digit: int) -> int:
        ans = 0
        for num in nums:
            x = num
            while x > 0:
                if x % 10 == digit:
                    ans += 1
                x //= 10
        return ans
