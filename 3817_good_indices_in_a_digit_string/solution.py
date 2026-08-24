# LeetCode 3817 - Good Indices in a Digit String
# https://leetcode.com/problems/good-indices-in-a-digit-string/

from typing import List


class Solution:
    def goodIndices(self, s: str) -> List[int]:
        ans = []
        for i in range(len(s)):
            t = str(i)
            k = len(t)
            if i + 1 - k >= 0 and s[i + 1 - k:i + 1] == t:
                ans.append(i)
        return ans
