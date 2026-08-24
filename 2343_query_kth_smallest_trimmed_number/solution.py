# LeetCode 2343 - Query Kth Smallest Trimmed Number
# https://leetcode.com/problems/query-kth-smallest-trimmed-number/

from typing import List


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n, m = len(nums), len(queries)
        ans = [0] * m
        for qi in range(m):
            k, trim = queries[qi][0], queries[qi][1]
            arr = []
            for i in range(n):
                s = nums[i]
                arr.append((s[len(s) - trim :], i))
            arr.sort(key=lambda x: (x[0], x[1]))
            ans[qi] = arr[k - 1][1]
        return ans
