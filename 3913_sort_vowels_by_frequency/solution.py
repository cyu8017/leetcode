# LeetCode 3913 - Sort Vowels By Frequency
# https://leetcode.com/problems/sort-vowels-by-frequency/

from typing import Dict, List


class Solution:
    def sortVowels(self, s: str) -> str:
        st = set(["a", "e", "i", "o", "u"])
        vowels: List[str] = []
        cnt: Dict[str, int] = {}
        for c in s:
            if c not in st:
                continue
            if c not in cnt:
                vowels.append(c)
                cnt[c] = 0
            cnt[c] += 1
        vowels.sort(key=lambda ch: -cnt[ch])
        ans = list(s)
        i = 0
        for k in range(len(s)):
            if s[k] not in st:
                continue
            ch = vowels[i]
            ans[k] = ch
            cnt[ch] -= 1
            if cnt[ch] == 0:
                i += 1
        return "".join(ans)
