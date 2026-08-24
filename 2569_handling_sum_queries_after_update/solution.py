# LeetCode 2569 - Handling Sum Queries After Update
# https://leetcode.com/problems/handling-sum-queries-after-update/

from typing import List


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        ones = [0] * (4 * n)
        lazy = [False] * (4 * n)

        def build(idx: int, l: int, r: int) -> None:
            if l == r:
                ones[idx] = nums1[l]
                return
            m = (l + r) >> 1
            build(idx * 2, l, m)
            build(idx * 2 + 1, m + 1, r)
            ones[idx] = ones[idx * 2] + ones[idx * 2 + 1]

        def apply(idx: int, l: int, r: int) -> None:
            ones[idx] = (r - l + 1) - ones[idx]
            lazy[idx] = not lazy[idx]

        def push(idx: int, l: int, r: int) -> None:
            if lazy[idx] and l != r:
                m = (l + r) >> 1
                apply(idx * 2, l, m)
                apply(idx * 2 + 1, m + 1, r)
                lazy[idx] = False

        def update(idx: int, l: int, r: int, ql: int, qr: int) -> None:
            if ql <= l and r <= qr:
                apply(idx, l, r)
                return
            push(idx, l, r)
            m = (l + r) >> 1
            if ql <= m:
                update(idx * 2, l, m, ql, qr)
            if qr > m:
                update(idx * 2 + 1, m + 1, r, ql, qr)
            ones[idx] = ones[idx * 2] + ones[idx * 2 + 1]

        build(1, 0, n - 1)
        sum2 = sum(nums2)
        ans = []
        for q in queries:
            if q[0] == 1:
                update(1, 0, n - 1, q[1], q[2])
            elif q[0] == 2:
                sum2 += q[1] * ones[1]
            else:
                ans.append(sum2)
        return ans
