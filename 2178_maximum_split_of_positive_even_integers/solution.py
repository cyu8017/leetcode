# LeetCode 2178 - Maximum Split of Positive Even Integers
# https://leetcode.com/problems/maximum-split-of-positive-even-integers/

from typing import List
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        ans = []
        x = 2
        while x <= finalSum:
            ans.append(x)
            finalSum -= x
            x += 2
        ans[len(ans) - 1] += finalSum
        return ans
