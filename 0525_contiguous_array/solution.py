# LeetCode 0525 - Contiguous Array
# https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        counts = {0: -1}
        balance = 0
        best = 0
        for index, num in enumerate(nums):
            balance += 1 if num == 1 else -1
            if balance in counts:
                best = max(best, index - counts[balance])
            else:
                counts[balance] = index
        return best
