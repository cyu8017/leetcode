# LeetCode 0605 - Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        bed = flowerbed[:]
        for i in range(len(bed)):
            if bed[i] == 1:
                continue
            left_empty = i == 0 or bed[i - 1] == 0
            right_empty = i == len(bed) - 1 or bed[i + 1] == 0
            if left_empty and right_empty:
                bed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False
