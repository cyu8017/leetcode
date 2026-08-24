# LeetCode 2085 - Count Common Words With One Occurrence
# https://leetcode.com/problems/count-common-words-with-one-occurrence/

from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        f1, f2 = {}, {}
        for w in words1:
            f1[w] = f1.get(w, 0) + 1
        for w in words2:
            f2[w] = f2.get(w, 0) + 1
        return sum(1 for k, v in f1.items() if v == 1 and f2.get(k, 0) == 1)
