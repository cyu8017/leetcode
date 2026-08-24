# LeetCode 3307 - Find the K-th Character in String Game II
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        shift = 0
        ops = operations[:]
        while ops:
            op = ops.pop()
            half = 1 << len(ops)
            if k > half:
                k = k - half
                if op == 1:
                    shift += 1
        return chr(97 + (shift % 26))
