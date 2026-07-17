# LeetCode 1852 - Distinct Numbers in Each Subarray
# https://leetcode.com/problems/distinct-numbers-in-each-subarray/

from collections import Counter
from typing import List


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums[:k])
        result = [len(counts)]
        left = 0

        for right in range(k, len(nums)):
            counts[nums[right]] += 1
            outgoing = nums[left]
            counts[outgoing] -= 1
            if counts[outgoing] == 0:
                del counts[outgoing]
            left += 1
            result.append(len(counts))

        return result
