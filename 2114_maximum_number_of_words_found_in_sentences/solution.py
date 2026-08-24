# LeetCode 2114 - Maximum Number of Words Found in Sentences
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

from typing import List
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for s in sentences:
            c = 1
            for i in range(len(s)):
                if s[i] == " ":
                    c += 1
            ans = max(ans, c)
        return ans
