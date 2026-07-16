from collections import Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = Counter(s[i:i + minSize] for i in range(len(s) - minSize + 1)
                         if len(set(s[i:i + minSize])) <= maxLetters)
        return max(counts.values(), default=0)
