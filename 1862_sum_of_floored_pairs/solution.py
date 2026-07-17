# LeetCode 1862 - Sum of Floored Pairs
# https://leetcode.com/problems/sum-of-floored-pairs/

from typing import List


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        max_val = max(nums)
        count = [0] * (max_val + 1)
        for num in nums:
            count[num] += 1

        prefix = [0] * (max_val + 1)
        prefix[0] = count[0]
        for value in range(1, max_val + 1):
            prefix[value] = prefix[value - 1] + count[value]

        answer = 0
        for divisor in range(1, max_val + 1):
            if count[divisor] == 0:
                continue
            quotient = 1
            while quotient * divisor <= max_val:
                low = quotient * divisor
                high = min((quotient + 1) * divisor - 1, max_val)
                matches = prefix[high] - (prefix[low - 1] if low else 0)
                answer = (answer + count[divisor] * matches * quotient) % mod
                quotient += 1

        return answer
