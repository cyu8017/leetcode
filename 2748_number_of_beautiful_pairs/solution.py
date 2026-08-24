# LeetCode 2748 - Number of Beautiful Pairs
# https://leetcode.com/problems/number-of-beautiful-pairs/

from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        def first_digit(x: int) -> int:
            while x >= 10:
                x //= 10
            return x

        ans = 0
        freq = [0] * 10
        for x in nums:
            last = x % 10
            for d in range(1, 10):
                if freq[d] > 0 and gcd(d, last) == 1:
                    ans += freq[d]
            freq[first_digit(x)] += 1
        return ans
