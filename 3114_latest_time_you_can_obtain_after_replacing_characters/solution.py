# LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/


class Solution:
    def findLatestTime(self, s: str) -> str:
        h = 11
        while True:
            for m in range(59, -1, -1):
                t = f"{h:02d}:{m:02d}"
                ok = True
                for i in range(5):
                    if s[i] != "?" and s[i] != t[i]:
                        ok = False
                        break
                if ok:
                    return t
            h -= 1
