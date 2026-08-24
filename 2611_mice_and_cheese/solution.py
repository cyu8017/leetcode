# LeetCode 2611 - Mice and Cheese
# https://leetcode.com/problems/mice-and-cheese/

from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        diff = [0] * n
        ans = 0
        for i in range(n):
            ans += reward2[i]
            diff[i] = reward1[i] - reward2[i]
        diff.sort(reverse=True)
        for i in range(k):
            ans += diff[i]
        return ans
