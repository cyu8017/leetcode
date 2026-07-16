# LeetCode 0483 - Smallest Good Base
# https://leetcode.com/problems/smallest-good-base/

import math


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        for length in range(int(math.log(num, 2)) + 1, 1, -1):
            low, high = 2, num - 1
            while low <= high:
                mid = (low + high) // 2
                total = 1
                power = 1
                ok = True
                for _ in range(length - 1):
                    power *= mid
                    total += power
                    if total > num:
                        ok = False
                        break
                if ok and total == num:
                    return str(mid)
                if not ok or total > num:
                    high = mid - 1
                else:
                    low = mid + 1
        return str(num - 1)
