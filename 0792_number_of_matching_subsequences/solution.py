# LeetCode 0792 - Number of Matching Subsequences
# https://leetcode.com/problems/number-of-matching-subsequences/

from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting: dict[str, list] = defaultdict(list)
        for word in words:
            it = iter(word)
            waiting[next(it)].append(it)

        count = 0
        for ch in s:
            advance = waiting[ch]
            waiting[ch] = []
            for it in advance:
                nxt = next(it, None)
                if nxt is None:
                    count += 1
                else:
                    waiting[nxt].append(it)
        return count
