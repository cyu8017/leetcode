# LeetCode 0737 - Sentence Similarity II
# https://leetcode.com/problems/sentence-similarity-ii/

from typing import List


class Solution:
    def areSentencesSimilarTwo(
        self,
        sentence1: List[str],
        sentence2: List[str],
        similarPairs: List[List[str]],
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        parent: dict[str, str] = {}

        def find(x: str) -> str:
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: str, b: str) -> None:
            parent[find(a)] = find(b)

        for a, b in similarPairs:
            union(a, b)

        for left, right in zip(sentence1, sentence2):
            if find(left) != find(right):
                return False
        return True
