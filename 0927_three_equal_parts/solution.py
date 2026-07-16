# LeetCode 0927 - Three Equal Parts
# https://leetcode.com/problems/three-equal-parts/

class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        ones = [i for i, bit in enumerate(arr) if bit]
        n = len(ones)
        if n % 3:
            return [-1, -1]
        if n == 0:
            return [0, len(arr) - 1]
        third = n // 3
        length = ones[-1] - ones[2 * third] + 1
        if (
            arr[ones[0] : ones[0] + length]
            == arr[ones[third] : ones[third] + length]
            == arr[ones[2 * third] :]
        ):
            return [ones[0] + length - 1, ones[third] + length]
        return [-1, -1]
