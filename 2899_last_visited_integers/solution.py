# LeetCode 2899 - Last Visited Integers
# https://leetcode.com/problems/last-visited-integers/

from typing import List


class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k = 0
        for v in nums:
            if v != -1:
                seen.append(v)
                k = 0
            else:
                k += 1
                if k > len(seen):
                    ans.append(-1)
                else:
                    ans.append(seen[-k])
        return ans
