# LeetCode 3948 - Lexicographically Maximum MEX Array
# https://leetcode.com/problems/lexicographically-maximum-mex-array/

from typing import List


class Solution:
    def maxMexArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        remaining = [0] * (n + 2)
        for x in nums:
            if x <= n + 1:
                remaining[x] += 1
        mex = 0
        while remaining[mex] > 0:
            mex += 1
        answer = []
        seen = [0] * (n + 2)
        stamp = 0
        index = 0
        while index < n:
            if mex == 0:
                answer.append(0)
                x = nums[index]
                if x <= n + 1:
                    remaining[x] -= 1
                index += 1
                continue
            stamp += 1
            need = mex
            while need > 0:
                x = nums[index]
                if x < mex and seen[x] != stamp:
                    seen[x] = stamp
                    need -= 1
                if x <= n + 1:
                    remaining[x] -= 1
                index += 1
            answer.append(mex)
            mex = 0
            while remaining[mex] > 0:
                mex += 1
        return answer
