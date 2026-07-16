# LeetCode 0354 - Russian Doll Envelopes
# https://leetcode.com/problems/russian-doll-envelopes/

import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda item: (item[0], -item[1]))
        tails: list[int] = []

        for _, height in envelopes:
            index = bisect.bisect_left(tails, height)
            if index == len(tails):
                tails.append(height)
            else:
                tails[index] = height

        return len(tails)
