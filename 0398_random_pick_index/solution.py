# LeetCode 0398 - Random Pick Index
# https://leetcode.com/problems/random-pick-index/

import random
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.indices: dict[int, list[int]] = defaultdict(list)
        for index, value in enumerate(nums):
            self.indices[value].append(index)
        random.seed(35)

    def pick(self, target: int) -> int:
        return random.choice(self.indices[target])
