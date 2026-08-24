# LeetCode 3672 - Sum of Weighted Modes in Subarrays
# https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

from typing import List
import heapq


class Solution:
    def modeWeight(self, nums: List[int], k: int) -> int:
        cnt = {}
        pq = []

        def push(freq: int, val: int) -> None:
            heapq.heappush(pq, (-freq, val))

        def get_mode() -> int:
            while True:
                freq, val = -pq[0][0], pq[0][1]
                if cnt.get(val, 0) == freq:
                    return freq * val
                heapq.heappop(pq)

        for i in range(k):
            x = nums[i]
            cnt[x] = cnt.get(x, 0) + 1
            push(cnt[x], x)
        ans = get_mode()
        for i in range(k, len(nums)):
            x, y = nums[i], nums[i - k]
            cnt[x] = cnt.get(x, 0) + 1
            cnt[y] = cnt.get(y, 0) - 1
            push(cnt[x], x)
            push(cnt[y], y)
            ans += get_mode()
        return ans
