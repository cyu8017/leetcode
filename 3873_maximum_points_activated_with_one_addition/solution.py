# LeetCode 3873 - Maximum Points Activated With One Addition
# https://leetcode.com/problems/maximum-points-activated-with-one-addition/

from typing import Dict, List


class Solution:
    def maxActivated(self, points: List[List[int]]) -> int:
        p: Dict[int, int] = {}
        size: Dict[int, int] = {}

        def find(x: int) -> int:
            if x not in p:
                p[x] = x
                size[x] = 1
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def unite(a: int, b: int) -> bool:
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return False
            if size[pa] > size[pb]:
                p[pb] = pa
                size[pa] = size[pa] + size[pb]
            else:
                p[pa] = pb
                size[pb] = size[pb] + size[pa]
            return True

        m = 3000000000
        for pt in points:
            unite(pt[0], pt[1] + m)
        cnt: Dict[int, int] = {}
        for pt in points:
            r = find(pt[0])
            cnt[r] = cnt.get(r, 0) + 1
        mx1 = 0
        mx2 = 0
        for x in cnt.values():
            if mx1 < x:
                mx2 = mx1
                mx1 = x
            elif mx2 < x:
                mx2 = x
        return mx1 + mx2 + 1
