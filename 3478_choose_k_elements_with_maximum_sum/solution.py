# LeetCode 3478 - Choose K Elements With Maximum Sum
# https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

from typing import List


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        arr = [[nums1[i], nums2[i], i] for i in range(n)]
        arr.sort(key=lambda x: x[0])
        ans = [0] * n
        h: List[int] = []
        s = 0

        def push(v: int) -> None:
            h.append(v)
            h.sort()

        def poll() -> int:
            return h.pop(0)

        i = 0
        while i < n:
            v = arr[i][0]
            start = i
            while i < n and arr[i][0] == v:
                i += 1
            for t in range(start, i):
                ans[arr[t][2]] = s
            for t in range(start, i):
                push(arr[t][1])
                s += arr[t][1]
                if len(h) > k:
                    s -= poll()
        return ans
