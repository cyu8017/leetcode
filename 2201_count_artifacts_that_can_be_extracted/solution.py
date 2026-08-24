# LeetCode 2201 - Count Artifacts That Can Be Extracted
# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

from typing import List
class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dug = set()
        for d in dig:
            dug.add(str(d[0]) + "," + str(d[1]))
        ans = 0
        for a in artifacts:
            ok = True
            r = a[0]
            while r <= a[2] and ok:
                for c in range(a[1], (a[3]) + 1):
                    if str(r) + "," + str(c) not in dug:
                        ok = False
                        break
                r += 1
            if ok:
                ans += 1
        return ans
