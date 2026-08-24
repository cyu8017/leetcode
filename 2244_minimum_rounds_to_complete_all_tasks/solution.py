# LeetCode 2244 - Minimum Rounds to Complete All Tasks
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        ans = 0
        for c in freq.values():
            if c == 1:
                return -1
            ans += (c + 2) // 3
        return ans
