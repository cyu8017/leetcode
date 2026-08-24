# LeetCode 2273 - Find Resultant Array After Removing Anagrams
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def sig(w: str) -> List[int]:
            c = [0] * 26
            for ch in w:
                c[ord(ch) - 97] += 1
            return c

        def eq(a: List[int], b: List[int]) -> bool:
            return a == b

        ans = [words[0]]
        prev = sig(words[0])
        for i in range(1, len(words)):
            cur = sig(words[i])
            if not eq(cur, prev):
                ans.append(words[i])
                prev = cur
        return ans
