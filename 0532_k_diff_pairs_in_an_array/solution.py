# LeetCode 0532 - K-diff Pairs in an Array
# https://leetcode.com/problems/k-diff-pairs-in-an-array/

from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        freq = Counter(nums)
        pairs = 0
        for num in freq:
            if k == 0:
                if freq[num] > 1:
                    pairs += 1
            elif num + k in freq:
                pairs += 1
        return pairs
