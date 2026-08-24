# LeetCode 3805 - Count Caesar Cipher Pairs
# https://leetcode.com/problems/count-caesar-cipher-pairs/

from typing import List


class Solution:
    def countPairs(self, words: List[str]) -> int:
        cnt = {}
        for word in words:
            s = list(word)
            k = ord("z") - ord(s[0])
            for i in range(1, len(s)):
                s[i] = chr(97 + (ord(s[i]) - 97 + k) % 26)
            s[0] = "z"
            key = "".join(s)
            cnt[key] = cnt.get(key, 0) + 1
        ans = 0
        for v in cnt.values():
            ans += v * (v - 1) // 2
        return ans
