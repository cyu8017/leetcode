from typing import List

from collections import Counter

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(a, b):
            squares = Counter(x * x for x in a)
            products = Counter()
            for i in range(len(b)):
                for j in range(i + 1, len(b)):
                    products[b[i] * b[j]] += 1
            return sum(count * products[value] for value, count in squares.items())
        return count(nums1, nums2) + count(nums2, nums1)
