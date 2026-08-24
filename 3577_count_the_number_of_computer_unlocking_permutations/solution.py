# LeetCode 3577 - Count the Number of Computer Unlocking Permutations
# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 1000000007
        ans = 1
        for i in range(1, len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
            ans = ans * i % mod
        return ans
