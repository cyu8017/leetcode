# LeetCode 0888 - Fair Candy Swap
# https://leetcode.com/problems/fair-candy-swap/

class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        bob = set(bobSizes)
        for a in aliceSizes:
            if a - diff in bob:
                return [a, a - diff]
        return []
