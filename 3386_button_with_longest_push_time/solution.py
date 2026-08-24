# LeetCode 3386 - Button with Longest Push Time
# https://leetcode.com/problems/button-with-longest-push-time/

from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        best_t = events[0][1]
        best_i = events[0][0]
        for i in range(1, len(events)):
            t = events[i][1] - events[i - 1][1]
            if t > best_t or (t == best_t and events[i][0] < best_i):
                best_t = t
                best_i = events[i][0]
        return best_i
