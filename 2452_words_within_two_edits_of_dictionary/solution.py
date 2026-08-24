# LeetCode 2452 - Words Within Two Edits of Dictionary
# https://leetcode.com/problems/words-within-two-edits-of-dictionary/

from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for q in queries:
            ok = False
            for d in dictionary:
                diff = 0
                for i in range(len(q)):
                    if q[i] != d[i]:
                        diff += 1
                        if diff > 2:
                            break
                if diff <= 2:
                    ok = True
                    break
            if ok:
                ans.append(q)
        return ans
