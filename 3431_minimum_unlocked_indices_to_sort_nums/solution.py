# LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
# https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

from typing import List


class Solution:
    def minUnlockedIndices(self, nums: List[int], locked: List[int]) -> int:
        n = len(nums)
        need = False
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                need = True
                break
        if not need:
            return 0
        left, right = n, -1
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    if i < left:
                        left = i
                    if j > right:
                        right = j
        if right < left:
            return 0
        ans = 0
        for i in range(left, right + 1):
            if locked[i] == 1:
                ans += 1
        tmp = nums[:]
        lock = locked[:]
        for i in range(left, right + 1):
            lock[i] = 0
        changed = True
        while changed:
            changed = False
            for i in range(n - 1):
                if lock[i] == 0 and lock[i + 1] == 0 and tmp[i] > tmp[i + 1]:
                    tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
                    changed = True
        for i in range(1, n):
            if tmp[i] < tmp[i - 1]:
                return -1
        return ans
