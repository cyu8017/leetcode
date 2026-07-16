# LeetCode 0781 - Rabbits in Forest
# https://leetcode.com/problems/rabbits-in-forest/

from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = 0
        for answer, count in Counter(answers).items():
            group = answer + 1
            groups = (count + group - 1) // group
            total += groups * group
        return total
