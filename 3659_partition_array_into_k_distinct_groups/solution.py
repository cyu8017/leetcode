# LeetCode 3659 - Partition Array Into K-Distinct Groups
# https://leetcode.com/problems/partition-array-into-k-distinct-groups/

from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        m = n // k
        mx = max(nums)
        cnt = [0] * (mx + 1)
        for x in nums:
            cnt[x] += 1
            if cnt[x] > m:
                return False
        return True
