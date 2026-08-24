# LeetCode 2007 - Find Original Array From Doubled Array
# https://leetcode.com/problems/find-original-array-from-doubled-array/

from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        freq = {}
        for x in changed:
            freq[x] = freq.get(x, 0) + 1
        ans = []
        for x in changed:
            if freq.get(x, 0) == 0:
                continue
            freq[x] -= 1
            if freq.get(2 * x, 0) == 0:
                return []
            freq[2 * x] -= 1
            ans.append(x)
        return ans
