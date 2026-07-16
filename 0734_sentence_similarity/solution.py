# LeetCode 0734 - Sentence Similarity
# https://leetcode.com/problems/sentence-similarity/

from typing import List


class Solution:
    def areSentencesSimilar(
        self,
        sentence1: List[str],
        sentence2: List[str],
        similarPairs: List[List[str]],
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        pairs = {(a, b) for a, b in similarPairs} | {(b, a) for a, b in similarPairs}
        for left, right in zip(sentence1, sentence2):
            if left != right and (left, right) not in pairs:
                return False
        return True
