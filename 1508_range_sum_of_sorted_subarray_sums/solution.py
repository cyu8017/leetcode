# LeetCode 1508

class Solution:
    def rangeSum(self, nums, n, left, right):
        values = []
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                values.append(total)
        values.sort()
        return sum(values[left - 1:right]) % 1000000007
