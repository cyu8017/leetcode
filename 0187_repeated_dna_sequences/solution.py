# LeetCode 0187 - Repeated DNA Sequences
# https://leetcode.com/problems/repeated-dna-sequences/

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen: set[str] = set()
        repeated: set[str] = set()
        for i in range(len(s) - 9):
            sequence = s[i : i + 10]
            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)
        return list(repeated)
