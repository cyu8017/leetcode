# LeetCode 1324 - Print Words Vertically

from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        return ["".join(word[i] if i < len(word) else " " for word in words).rstrip()
                for i in range(max(map(len, words)))]
