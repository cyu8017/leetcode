# LeetCode 2301 - Match Substring After Replacement
# https://leetcode.com/problems/match-substring-after-replacement/

from typing import List


class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        allow = set()
        for a, b in mappings:
            allow.add((ord(a[0]) << 8) | ord(b[0]))
        n = len(s)
        mlen = len(sub)
        for i in range(n - mlen + 1):
            ok = True
            for j in range(mlen):
                a, b = s[i + j], sub[j]
                if a == b or ((ord(b) << 8) | ord(a)) in allow:
                    continue
                ok = False
                break
            if ok:
                return True
        return False
