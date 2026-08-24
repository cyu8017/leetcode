# LeetCode 3510 - Minimum Pair Removal to Sort Array II
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

from typing import List, Optional, Set


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        inv = ans = 0
        sl: List[List[int]] = []
        idx: Set[int] = set(range(n))

        def key(sm: int, i: int) -> int:
            return sm * 1000000007 + i

        sl_map = {}

        def addSl(sm: int, i: int) -> None:
            sl_map[key(sm, i)] = [sm, i]
            lo, hi = 0, len(sl)
            while lo < hi:
                mid = (lo + hi) >> 1
                if sl[mid][0] < sm or (sl[mid][0] == sm and sl[mid][1] < i):
                    lo = mid + 1
                else:
                    hi = mid
            sl.insert(lo, [sm, i])

        def remSl(sm: int, i: int) -> None:
            k = key(sm, i)
            if k not in sl_map:
                return
            del sl_map[k]
            for t in range(len(sl)):
                if sl[t][0] == sm and sl[t][1] == i:
                    sl.pop(t)
                    break

        def ceiling(st: Set[int], x: int) -> Optional[int]:
            best = None
            for v in st:
                if v >= x and (best is None or v < best):
                    best = v
            return best

        def floor(st: Set[int], x: int) -> Optional[int]:
            best = None
            for v in st:
                if v <= x and (best is None or v > best):
                    best = v
            return best

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                inv += 1
            addSl(nums[i] + nums[i + 1], i)
        while inv > 0:
            ans += 1
            p = sl.pop(0)
            sl_map.pop(key(p[0], p[1]), None)
            s, i = p[0], p[1]
            j = ceiling(idx, i + 1)
            if nums[i] > nums[j]:
                inv -= 1
            h = floor(idx, i - 1)
            if h is not None:
                if nums[h] > nums[i]:
                    inv -= 1
                remSl(nums[h] + nums[i], h)
                if nums[h] > s:
                    inv += 1
                addSl(nums[h] + s, h)
            kk = ceiling(idx, j + 1)
            if kk is not None:
                if nums[j] > nums[kk]:
                    inv -= 1
                remSl(nums[j] + nums[kk], j)
                if s > nums[kk]:
                    inv += 1
                addSl(s + nums[kk], i)
            nums[i] = s
            idx.discard(j)
        return ans
