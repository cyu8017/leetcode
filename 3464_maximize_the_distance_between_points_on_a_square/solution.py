# LeetCode 3464 - Maximize the Distance Between Points on a Square
# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

from typing import List


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def can_place(arr: List[int], perim: int, mid: int) -> bool:
            n = len(arr)
            for s in range(n):
                cnt = 1
                last = arr[s]
                idx = s
                while cnt < k:
                    target = last + mid
                    found = False
                    for step in range(1, n):
                        ni = (idx + step) % n
                        val = arr[ni]
                        add = perim if ni <= idx else 0
                        if val + add >= target:
                            last = val + add
                            idx = ni
                            cnt += 1
                            found = True
                            break
                    if not found:
                        break
                if cnt == k and last - arr[s] <= perim - mid:
                    return True
            return False

        arr = [0] * len(points)
        for i, (x, y) in enumerate(points):
            if y == 0:
                d = x
            elif x == side:
                d = side + y
            elif y == side:
                d = 2 * side + (side - x)
            else:
                d = 3 * side + (side - y)
            arr[i] = d
        arr.sort()
        perim = 4 * side
        lo, hi = 0, 2 * side
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_place(arr, perim, mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
