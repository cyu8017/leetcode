# LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
# https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        unique = sorted(nums)
        u = 0
        for i in range(len(unique)):
            if u == 0 or unique[i] != unique[u - 1]:
                unique[u] = unique[i]
                u += 1
        unique = unique[:u]
        self.unique = unique
        rank = [0] * n
        global_count = [0] * (len(unique) + 1)
        global_sum = [0] * (len(unique) + 1)
        for i in range(n):
            rank[i] = self.lowerBound(unique, nums[i]) + 1
            self.add(global_count, global_sum, rank[i], 1)
        answer = -(1 << 60)
        for left in range(n):
            inside_count = [0] * (len(unique) + 1)
            inside_sum = [0] * (len(unique) + 1)
            outside_count = global_count[:]
            outside_sum = global_sum[:]
            subarray_sum = 0
            for right in range(left, n):
                self.add(outside_count, outside_sum, rank[right], -1)
                self.add(inside_count, inside_sum, rank[right], 1)
                subarray_sum += nums[right]
                inside_size = right - left + 1
                outside_size = n - inside_size
                limit = min(k, min(inside_size, outside_size))
                low, high = 0, limit
                while low < high:
                    mid = (low + high + 1) // 2
                    inside_value = unique[self.kth(inside_count, mid) - 1]
                    outside_order = outside_size - mid + 1
                    outside_value = unique[self.kth(outside_count, outside_order) - 1]
                    if outside_value > inside_value:
                        low = mid
                    else:
                        high = mid - 1
                swaps = low
                gain = 0
                if swaps > 0:
                    small_inside = self.sumSmallest(inside_count, inside_sum, swaps)
                    total_outside = self.querySum(outside_sum, len(unique))
                    large_outside = total_outside - self.sumSmallest(outside_count, outside_sum, outside_size - swaps)
                    gain = large_outside - small_inside
                answer = max(answer, subarray_sum + gain)
        return answer

    def add(self, count: List[int], s: List[int], index: int, delta: int) -> None:
        value = self.unique[index - 1]
        while index < len(count):
            count[index] += delta
            s[index] += delta * value
            index += index & -index

    def queryCount(self, bit: List[int], index: int) -> int:
        result = 0
        while index > 0:
            result += bit[index]
            index -= index & -index
        return result

    def querySum(self, bit: List[int], index: int) -> int:
        result = 0
        while index > 0:
            result += bit[index]
            index -= index & -index
        return result

    def kth(self, bit: List[int], order: int) -> int:
        index = 0
        step = 1
        while (step << 1) < len(bit):
            step <<= 1
        while step > 0:
            nxt = index + step
            if nxt < len(bit) and bit[nxt] < order:
                index = nxt
                order -= bit[nxt]
            step >>= 1
        return index + 1

    def sumSmallest(self, count: List[int], s: List[int], amount: int) -> int:
        if amount <= 0:
            return 0
        index = self.kth(count, amount)
        count_before = self.queryCount(count, index - 1)
        sum_before = self.querySum(s, index - 1)
        return sum_before + (amount - count_before) * self.unique[index - 1]

    def lowerBound(self, a: List[int], x: int) -> int:
        lo, hi = 0, len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo
