# LeetCode 0784 - Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation/

from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [""]
        for ch in s:
            if ch.isalpha():
                result = [prefix + c for prefix in result for c in (ch.lower(), ch.upper())]
            else:
                result = [prefix + ch for prefix in result]
        return result
