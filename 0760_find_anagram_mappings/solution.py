# LeetCode 0760 - Find Anagram Mappings
# https://leetcode.com/problems/find-anagram-mappings/

from collections import defaultdict, deque
from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        positions: dict[int, deque[int]] = defaultdict(deque)
        for index, value in enumerate(nums2):
            positions[value].append(index)
        return [positions[value].popleft() for value in nums1]
