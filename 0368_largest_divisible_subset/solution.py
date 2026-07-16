# LeetCode 0368 - Largest Divisible Subset
# https://leetcode.com/problems/largest-divisible-subset/

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        chains: dict[int, list[int]] = {num: [num] for num in nums}
        best: list[int] = []

        for num in nums:
            for prev in chains:
                if prev < num and num % prev == 0 and len(chains[prev]) + 1 > len(chains[num]):
                    chains[num] = chains[prev] + [num]
            if len(chains[num]) > len(best):
                best = chains[num]

        return best
