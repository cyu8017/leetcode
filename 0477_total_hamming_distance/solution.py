# LeetCode 0477 - Total Hamming Distance
# https://leetcode.com/problems/total-hamming-distance/


class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        total = 0
        for bit in range(32):
            zeros = ones = 0
            for value in nums:
                if value & (1 << bit):
                    ones += 1
                else:
                    zeros += 1
            total += zeros * ones
        return total
