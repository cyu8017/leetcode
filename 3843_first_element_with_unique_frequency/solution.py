# LeetCode 3843 - First Element with Unique Frequency
# https://leetcode.com/problems/first-element-with-unique-frequency/

from typing import List


class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        freq = {}
        for v in cnt.values():
            freq[v] = freq.get(v, 0) + 1
        for x in nums:
            if freq[cnt[x]] == 1:
                return x
        return -1
