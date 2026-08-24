# LeetCode 3008 - Find Beautiful Indices in the Given Array II
# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/

from typing import List


def buildLPS(lps: List[int], pattern: str) -> None:
    l = 0
    i = 1
    s_l = len(pattern)
    lps[0] = 0
    while i < s_l:
        if pattern[i] == pattern[l]:
            l += 1
            lps[i] = l
            i += 1
        elif l != 0:
            l = lps[l - 1]
        else:
            lps[i] = l
            i += 1


def kmp(s: str, pat: str, lps: List[int], index: List[int]) -> None:
    s_len = len(s)
    pat_l = len(pat)
    i = 0
    j = 0
    while s_len - i >= pat_l - j:
        if s[i] == pat[j]:
            i += 1
            j += 1
        if j == pat_l:
            index.append(i - pat_l)
            j = lps[j - 1]
        elif i < s_len and s[i] != pat[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a_len = len(a)
        b_len = len(b)
        lps_a = [0] * a_len
        lps_b = [0] * b_len
        a_index = []
        b_index = []
        result = []
        buildLPS(lps_a, a)
        buildLPS(lps_b, b)
        kmp(s, a, lps_a, a_index)
        kmp(s, b, lps_b, b_index)
        i = 0
        j = 0
        while i < len(a_index) and j < len(b_index):
            if a_index[i] + k >= b_index[j] and a_index[i] - k <= b_index[j]:
                result.append(a_index[i])
                i += 1
            elif a_index[i] - k > b_index[j]:
                j += 1
            else:
                i += 1
        return result
