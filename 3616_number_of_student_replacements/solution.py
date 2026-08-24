# LeetCode 3616 - Number of Student Replacements
# https://leetcode.com/problems/number-of-student-replacements/

from typing import List


class Solution:
    def totalReplacements(self, ranks: List[int]) -> int:
        ans = 0
        cur = ranks[0]
        for x in ranks:
            if x < cur:
                cur = x
                ans += 1
        return ans
