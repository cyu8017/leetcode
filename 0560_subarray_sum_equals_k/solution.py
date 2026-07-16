# LeetCode 0560 - Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts: dict[int, int] = defaultdict(int)
        counts[0] = 1
        prefix = 0
        answer = 0
        for num in nums:
            prefix += num
            answer += counts[prefix - k]
            counts[prefix] += 1
        return answer
