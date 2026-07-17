# LeetCode 1865 - Finding Pairs With a Certain Sum
# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

from collections import Counter
from typing import List


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counts = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.counts[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.counts[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(self.counts[tot - num] for num in self.nums1)
