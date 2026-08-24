# LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
# https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

from typing import List


def calc3587(pos: List[List[int]], n: int, k: int) -> int:
    res = 0
    for i in range(0, n, 2):
        res += abs(pos[k][i // 2] - i)
    return res


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        pos = [[], []]
        for i, x in enumerate(nums):
            pos[x & 1].append(i)
        if abs(len(pos[0]) - len(pos[1])) > 1:
            return -1
        if len(pos[0]) > len(pos[1]):
            return calc3587(pos, len(nums), 0)
        if len(pos[0]) < len(pos[1]):
            return calc3587(pos, len(nums), 1)
        return min(calc3587(pos, len(nums), 0), calc3587(pos, len(nums), 1))
