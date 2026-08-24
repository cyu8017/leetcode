# LeetCode 2234 - Maximum Total Beauty of the Gardens
# https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

from typing import List


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        for i in range(n):
            if flowers[i] > target:
                flowers[i] = target
        flowers.sort()
        s = sum(flowers)
        if target * n - s <= newFlowers:
            return n * full
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + flowers[i]
        ans = 0
        j = n - 1
        remain = newFlowers
        for complete in range(n + 1):
            if complete > 0:
                need = target - flowers[n - complete]
                if remain < need:
                    break
                remain -= need
            while j >= n - complete or (j >= 0 and flowers[j] * (j + 1) - pref[j + 1] > remain):
                j -= 1
            partial_val = 0
            if j >= 0:
                extra = (remain - (flowers[j] * (j + 1) - pref[j + 1])) // (j + 1)
                partial_val = flowers[j] + extra
                if partial_val >= target:
                    partial_val = target - 1
            ans = max(ans, complete * full + partial_val * partial)
        return ans
