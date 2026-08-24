# LeetCode 3926 - Count Valid Word Occurrences
# https://leetcode.com/problems/count-valid-word-occurrences/

from typing import Dict, List


class Solution:
    def countWordOccurrences(self, chunks: List[str], queries: List[str]) -> List[int]:
        sb = ""
        for c in chunks:
            sb += c
        s = sb
        n = len(s)
        cnt: Dict[str, int] = {}
        i = 0
        while i < n:
            if s[i] == " " or s[i] == "-":
                i += 1
                continue
            j = i
            while j < n and s[j] != " " and (s[j] != "-" or (j + 1 < n and s[j + 1] != " " and s[j + 1] != "-")):
                j += 1
            word = s[i:j]
            cnt[word] = cnt.get(word, 0) + 1
            i = j
        ans = [0] * len(queries)
        for k in range(len(queries)):
            ans[k] = cnt.get(queries[k], 0)
        return ans
