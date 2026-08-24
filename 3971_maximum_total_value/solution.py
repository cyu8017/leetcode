# LeetCode 3971 - Maximum Total Value
# https://leetcode.com/problems/maximum-total-value/

from typing import List


class Solution:
    def maximumTotalValue(self, value: List[int], decay: List[int], m: int) -> int:
        mod = 1000000007
        if self.countAtLeast(value, decay, 1) <= m:
            s = 0
            for i in range(len(value)):
                terms = (value[i] - 1) // decay[i] + 1
                s = (s + terms * value[i] - decay[i] * terms * (terms - 1) // 2) % mod
            return s
        high = 0
        for v in value:
            if v > high:
                high = v
        low = 1
        while low < high:
            mid = (low + high + 1) // 2
            if self.countAtLeast(value, decay, mid) >= m:
                low = mid
            else:
                high = mid - 1
        threshold = low
        count = 0
        s = 0
        for i in range(len(value)):
            if value[i] < threshold:
                continue
            terms = (value[i] - threshold) // decay[i] + 1
            count += terms
            s = (s + (terms * value[i] - decay[i] * terms * (terms - 1) // 2) % mod) % mod
        s = (s - ((count - m) % mod) * (threshold % mod)) % mod
        if s < 0:
            s += mod
        return s

    def countAtLeast(self, value: List[int], decay: List[int], threshold: int) -> int:
        count = 0
        for i in range(len(value)):
            if value[i] >= threshold:
                count += (value[i] - threshold) // decay[i] + 1
        return count
