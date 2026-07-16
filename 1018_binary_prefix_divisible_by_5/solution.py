# LeetCode 1018 - Binary Prefix Divisible By 5
# https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        ans = []
        rem = 0
        for bit in nums:
            rem = (rem * 2 + bit) % 5
            ans.append(rem == 0)
        return ans
