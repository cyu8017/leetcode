# LeetCode 3485 - Longest Common Prefix of K Strings After Removal
# https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

from typing import List


class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        def lcp_of(a: List[str]) -> int:
            if not a:
                return 0
            pref = a[0]
            for t in range(1, len(a)):
                s = a[t]
                i = 0
                while i < len(pref) and i < len(s) and pref[i] == s[i]:
                    i += 1
                pref = pref[:i]
                if not pref:
                    return 0
            return len(pref)

        n = len(words)
        ans = [0] * n
        for i in range(n):
            rest = [words[j] for j in range(n) if j != i]
            if len(rest) < k:
                ans[i] = 0
                continue
            rest.sort()
            best = 0
            for j in range(len(rest) - k + 1):
                best = max(best, lcp_of(rest[j : j + k]))
            ans[i] = best
        return ans
