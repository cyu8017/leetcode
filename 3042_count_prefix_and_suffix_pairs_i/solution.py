# LeetCode 3042 - Count Prefix and Suffix Pairs I
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)):
            s = words[i]
            for j in range(i + 1, len(words)):
                t = words[j]
                if len(t) >= len(s) and t.startswith(s) and t.endswith(s):
                    ans += 1
        return ans
