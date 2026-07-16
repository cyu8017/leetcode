# LeetCode 0384 - Shuffle an Array
# https://leetcode.com/problems/shuffle-an-array/

import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.original = list(nums)
        random.seed(47)

    def reset(self) -> List[int]:
        return list(self.original)

    def shuffle(self) -> List[int]:
        result = list(self.original)
        random.shuffle(result)
        return result
