# LeetCode 0347 - Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]

        for value, count in counts.items():
            buckets[count].append(value)

        result: list[int] = []
        for index in range(len(buckets) - 1, -1, -1):
            for value in buckets[index]:
                result.append(value)
                if len(result) == k:
                    return result

        return result
