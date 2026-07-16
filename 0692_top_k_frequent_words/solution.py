# LeetCode 0692 - Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        ordered = sorted(counts.keys(), key=lambda w: (-counts[w], w))
        return ordered[:k]
