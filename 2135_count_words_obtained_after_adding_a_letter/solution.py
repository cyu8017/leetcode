# LeetCode 2135 - Count Words Obtained After Adding a Letter
# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

from typing import List
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def mask(w):
            m = 0
            for i in range(len(w)):
                m |= 1 << (ord(w[i]) - 97)
            return m

        have = set()
        for w in startWords:
            have.add(mask(w))
        ans = 0
        for w in targetWords:
            m = mask(w)
            for i in range(len(w)):
                if m ^ (1 << (ord(w[i]) - 97)) in have:
                    ans += 1
                    break
        return ans
