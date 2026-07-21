from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = Counter(s).values()
        return len(set(freq)) == 1
