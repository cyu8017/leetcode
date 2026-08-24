# LeetCode 2511 - Maximum Enemy Forts That Can Be Captured
# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans = 0
        prev = -1
        for i in range(len(forts)):
            if forts[i] != 0:
                if prev >= 0 and forts[prev] == -forts[i]:
                    if i - prev - 1 > ans:
                        ans = i - prev - 1
                prev = i
        return ans
