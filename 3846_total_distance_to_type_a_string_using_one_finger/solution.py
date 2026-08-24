# LeetCode 3846 - Total Distance To Type A String Using One Finger
# https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

from typing import Dict, List, Tuple

_POS: Dict[str, Tuple[int, int]] = {}
_KEYS = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
for _i in range(3):
    for _j in range(len(_KEYS[_i])):
        _POS[_KEYS[_i][_j]] = (_i, _j)


class Solution:
    def totalDistance(self, s: str) -> int:
        pre = "a"
        ans = 0
        for cur in s:
            p1 = _POS[pre]
            p2 = _POS[cur]
            ans += abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            pre = cur
        return ans
