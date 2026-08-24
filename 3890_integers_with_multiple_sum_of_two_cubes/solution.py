# LeetCode 3890 - Integers With Multiple Sum Of Two Cubes
# https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

from typing import Dict, List, Optional

GOOD3890: Optional[List[int]] = None


def init3890() -> None:
    global GOOD3890
    if GOOD3890 is not None:
        return
    LIMIT = 1000000000
    cnt: Dict[int, int] = {}
    cubes = [0] * 1001
    for i in range(1001):
        cubes[i] = i * i * i
    for a in range(1, 1001):
        for b in range(a, 1001):
            x = cubes[a] + cubes[b]
            if x > LIMIT:
                break
            cnt[x] = cnt.get(x, 0) + 1
    GOOD3890 = []
    for k, v in cnt.items():
        if v > 1:
            GOOD3890.append(k)
    GOOD3890.sort()


class Solution:
    def findGoodIntegers(self, n: int) -> List[int]:
        init3890()
        lo = 0
        hi = len(GOOD3890)
        while lo < hi:
            mid = (lo + hi) // 2
            if GOOD3890[mid] <= n:
                lo = mid + 1
            else:
                hi = mid
        return GOOD3890[:lo]
