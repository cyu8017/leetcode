# LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
# https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        cur = ""
        for ch in target:
            cur += "a"
            ans.append(cur)
            while cur[-1] != ch:
                last = chr(ord(cur[-1]) + 1)
                cur = cur[:-1] + last
                ans.append(cur)
        return ans
