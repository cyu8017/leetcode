# LeetCode 1151 - Minimum Swaps to Group All 1's Together
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

class Solution:
    def minSwaps(self, data: list[int]) -> int:
        ones = sum(data)
        if ones <= 1:
            return 0
        cur = sum(data[:ones])
        best = cur
        for i in range(ones, len(data)):
            cur += data[i] - data[i - ones]
            best = max(best, cur)
        return ones - best
