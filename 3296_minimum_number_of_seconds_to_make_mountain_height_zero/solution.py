# LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

from typing import List


def ok(t: int, mountainHeight: int, workerTimes: List[int]) -> bool:
    total = 0
    for w in workerTimes:
        l, h = 0, mountainHeight
        while l < h:
            mid = (l + h + 1) // 2
            if w * mid * (mid + 1) // 2 <= t:
                l = mid
            else:
                h = mid - 1
        total += l
        if total >= mountainHeight:
            return True
    return total >= mountainHeight


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        lo, hi = 0, 10**18
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid, mountainHeight, workerTimes):
                hi = mid
            else:
                lo = mid + 1
        return lo
