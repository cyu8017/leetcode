# LeetCode 3080 - Mark Elements on Array by Performing Queries
# https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

from typing import List


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        s = 0
        for x in nums:
            s += x
        mark = [False] * n
        arr = [[v, i] for i, v in enumerate(nums)]
        arr.sort(key=lambda a: (a[0], a[1]))
        ans = [0] * len(queries)
        j = 0
        for qi in range(len(queries)):
            index = queries[qi][0]
            k = queries[qi][1]
            if not mark[index]:
                mark[index] = True
                s -= nums[index]
            while k > 0 and j < n:
                if not mark[arr[j][1]]:
                    mark[arr[j][1]] = True
                    s -= arr[j][0]
                    k -= 1
                j += 1
            ans[qi] = s
        return ans
