# LeetCode 2386 - Find the K-Sum of an Array
# https://leetcode.com/problems/find-the-k-sum-of-an-array/

from typing import List


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        total = 0
        n = len(nums)
        abs_nums = [0] * n
        for i in range(n):
            if nums[i] >= 0:
                total += nums[i]
                abs_nums[i] = nums[i]
            else:
                abs_nums[i] = -nums[i]
        abs_nums.sort()
        h = []

        def push(item):
            h.append(item)
            i = len(h) - 1
            while i > 0:
                p = (i - 1) >> 1
                if h[p][0] >= h[i][0]:
                    break
                h[p], h[i] = h[i], h[p]
                i = p

        def pop():
            top = h[0]
            last = h.pop()
            if h:
                h[0] = last
                i = 0
                while True:
                    largest = i
                    l, r = i * 2 + 1, i * 2 + 2
                    if l < len(h) and h[l][0] > h[largest][0]:
                        largest = l
                    if r < len(h) and h[r][0] > h[largest][0]:
                        largest = r
                    if largest == i:
                        break
                    h[largest], h[i] = h[i], h[largest]
                    i = largest
            return top

        push([total, 0])
        for _ in range(k - 1):
            cur = pop()
            s, i = cur[0], cur[1]
            if i >= len(abs_nums):
                continue
            push([s - abs_nums[i], i + 1])
            if i > 0:
                push([s - abs_nums[i] + abs_nums[i - 1], i + 1])
        return h[0][0]
