# LeetCode 0220 - Contains Duplicate III
# https://leetcode.com/problems/contains-duplicate-iii/

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False
        width = valueDiff + 1
        buckets: dict[int, int] = {}

        def bucket_id(num: int) -> int:
            return num // width if num >= 0 else (num + 1) // width - 1

        for i, num in enumerate(nums):
            bucket = bucket_id(num)
            if bucket in buckets:
                return True
            if bucket - 1 in buckets and abs(num - buckets[bucket - 1]) <= valueDiff:
                return True
            if bucket + 1 in buckets and abs(num - buckets[bucket + 1]) <= valueDiff:
                return True
            if len(buckets) >= indexDiff:
                old = nums[i - indexDiff]
                del buckets[bucket_id(old)]
            buckets[bucket] = num
        return False
