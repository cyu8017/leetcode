from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.values = {i: x for i, x in enumerate(nums) if x}

    def dotProduct(self, vec: "SparseVector") -> int:
        if len(self.values) > len(vec.values):
            return vec.dotProduct(self)
        return sum(x * vec.values.get(i, 0) for i, x in self.values.items())

class Solution:
    def dotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        return SparseVector(nums1).dotProduct(SparseVector(nums2))
