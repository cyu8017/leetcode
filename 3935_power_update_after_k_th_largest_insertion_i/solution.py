# LeetCode 3935 - Power Update After K Th Largest Insertion I
# https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

from typing import Dict, List, Optional


def merge(st: Dict[int, int], x: int, v: int) -> None:
    c = st.get(x, 0)
    if c + v == 0:
        st.pop(x, None)
    else:
        st[x] = c + v


def firstKey(st: Dict[int, int]) -> Optional[int]:
    best = None
    for k in st:
        if best is None or k < best:
            best = k
    return best


def lastKey(st: Dict[int, int]) -> Optional[int]:
    best = None
    for k in st:
        if best is None or k > best:
            best = k
    return best


def qpow(a: int, b: int, mod: int) -> int:
    ans = 1
    a = int(a)
    while b > 0:
        if (b & 1) != 0:
            ans = (ans * a) % mod
        a = (a * a) % mod
        b >>= 1
    return ans


class Solution:
    def powerUpdate(self, nums: List[int], p: int, queries: List[List[int]]) -> List[int]:
        L: Dict[int, int] = {}
        R: Dict[int, int] = {}
        sz1 = 0
        sz2 = len(nums)
        for x in nums:
            merge(R, x, 1)
        mod = 1000000007
        ans = [0] * len(queries)
        for qi in range(len(queries)):
            val, k = queries[qi][0], queries[qi][1]
            merge(R, val, 1)
            sz2 += 1
            node = firstKey(R)
            merge(R, node, -1)
            sz2 -= 1
            merge(L, node, 1)
            sz1 += 1
            while sz2 < k:
                node = lastKey(L)
                merge(L, node, -1)
                sz1 -= 1
                merge(R, node, 1)
                sz2 += 1
            while sz2 > k:
                node = firstKey(R)
                merge(R, node, -1)
                sz2 -= 1
                merge(L, node, 1)
                sz1 += 1
            x = firstKey(R)
            p = qpow(p, x, mod)
            ans[qi] = p
        return ans
