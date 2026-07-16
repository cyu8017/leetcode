# LeetCode 0995 - Minimum Number of K Consecutive Bit Flips
# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        n = len(nums)
        flip = [0] * n
        ans = flipped = 0
        for i, bit in enumerate(nums):
            if i >= k:
                flipped ^= flip[i - k]
            if bit == flipped:
                if i + k > n:
                    return -1
                ans += 1
                flipped ^= 1
                flip[i] = 1
        return ans
