# LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
# https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

from typing import List


class State:
    def __init__(self, value: int = 0, count: int = 0):
        self.value = value
        self.count = count


def better(a: State, b: State) -> bool:
    return a.value > b.value or (a.value == b.value and a.count > b.count)


def candidate_better(dp: List[State], prefix: List[int], a: int, b: int) -> bool:
    left = State(dp[a].value - prefix[a], dp[a].count)
    right = State(dp[b].value - prefix[b], dp[b].count)
    return better(left, right)


def run(prefix: List[int], n: int, l: int, r: int, penalty: int) -> State:
    dp = [State() for _ in range(n + 1)]
    deque = []
    for end in range(1, n + 1):
        add_index = end - l
        if add_index >= 0:
            while deque and candidate_better(dp, prefix, add_index, deque[-1]):
                deque.pop()
            deque.append(add_index)
        min_index = end - r
        while deque and deque[0] < min_index:
            deque.pop(0)
        dp[end] = State(dp[end - 1].value, dp[end - 1].count)
        if deque:
            start = deque[0]
            take = State(dp[start].value + prefix[end] - prefix[start] - penalty, dp[start].count + 1)
            if better(take, dp[end]):
                dp[end] = take
    return dp[n]


class Solution:
    def maxSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        unconstrained = run(prefix, n, l, r, 0)
        if unconstrained.count > 0 and unconstrained.count <= m:
            return unconstrained.value
        if unconstrained.count > m:
            bound = 0
            for value in nums:
                bound += value if value >= 0 else -value
            low, high = 0, bound + 1
            while low < high:
                mid = low + (high - low + 1) // 2
                if run(prefix, n, l, r, mid).count >= m:
                    low = mid
                else:
                    high = mid - 1
            state = run(prefix, n, l, r, low)
            return state.value + low * m
        infinity = 2 ** 60
        best_single = -infinity
        deque = []
        for end in range(1, n + 1):
            add_index = end - l
            if add_index >= 0:
                while deque and prefix[deque[-1]] >= prefix[add_index]:
                    deque.pop()
                deque.append(add_index)
            min_index = end - r
            while deque and deque[0] < min_index:
                deque.pop(0)
            if deque:
                s = prefix[end] - prefix[deque[0]]
                if s > best_single:
                    best_single = s
        return best_single
