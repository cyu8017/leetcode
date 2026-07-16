# LeetCode 0698 - Partition to K Equal Sum Subsets
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        buckets = [0] * k

        def dfs(index: int) -> bool:
            if index == len(nums):
                return True
            for i in range(k):
                if buckets[i] + nums[index] > target:
                    continue
                buckets[i] += nums[index]
                if dfs(index + 1):
                    return True
                buckets[i] -= nums[index]
                if buckets[i] == 0:
                    break
            return False

        return dfs(0)
