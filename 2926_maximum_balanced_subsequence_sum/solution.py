# LeetCode 2926 - Maximum Balanced Subsequence Sum
# https://leetcode.com/problems/maximum-balanced-subsequence-sum/

from typing import List


class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        neg_inf = -(2**53) // 4
        n = len(nums)
        keys = [v - i for i, v in enumerate(nums)]
        uniq = sorted(set(keys))
        bit = [neg_inf] * (len(uniq) + 2)

        def idx_of(v: int) -> int:
            lo, hi = 0, len(uniq)
            while lo < hi:
                mid = (lo + hi) // 2
                if uniq[mid] < v:
                    lo = mid + 1
                else:
                    hi = mid
            return lo + 1

        def update(i: int, val: int) -> None:
            while i < len(bit):
                if val > bit[i]:
                    bit[i] = val
                i += i & -i

        def query(i: int) -> int:
            best = neg_inf
            while i > 0:
                if bit[i] > best:
                    best = bit[i]
                i -= i & -i
            return best

        ans = neg_inf
        for i in range(n):
            id_ = idx_of(keys[i])
            best = query(id_)
            cur = nums[i]
            if best > neg_inf / 2:
                cand = best + nums[i]
                if cand > cur:
                    cur = cand
            update(id_, cur)
            if cur > ans:
                ans = cur
        return ans
