# LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
# https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

from typing import List


def canFinish(w1: str, w2: str, i: int, j: int, usedSkip: bool, right: List[int]) -> bool:
    m = len(w2)
    if j >= m:
        return True
    if not usedSkip:
        if right[j] >= i:
            return True
        if j + 1 <= m and right[j + 1] > i:
            return True
        if right[j] > i:
            return True
        return False
    return right[j] >= i


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        right = [0] * (m + 1)
        right[m] = n
        j = m - 1
        i = n - 1
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                right[j] = i
                j -= 1
            i -= 1
        while j >= 0:
            right[j] = -1
            j -= 1
        ans = [0] * m
        usedSkip = False
        i = 0
        for j in range(m):
            found = False
            while i < n:
                if word1[i] == word2[j]:
                    if canFinish(word1, word2, i + 1, j + 1, usedSkip, right):
                        ans[j] = i
                        i += 1
                        found = True
                        break
                elif not usedSkip:
                    if canFinish(word1, word2, i + 1, j + 1, True, right):
                        ans[j] = i
                        i += 1
                        usedSkip = True
                        found = True
                        break
                i += 1
            if not found:
                return []
        return ans
