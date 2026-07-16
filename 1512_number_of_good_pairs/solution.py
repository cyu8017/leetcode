# LeetCode 1512

class Solution:
    def numIdenticalPairs(self, nums):
        from collections import Counter
        return sum(n * (n - 1) // 2 for n in Counter(nums).values())
