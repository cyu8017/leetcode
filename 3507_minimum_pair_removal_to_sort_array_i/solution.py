# LeetCode 3507 - Minimum Pair Removal to Sort Array I
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

from typing import List


def isNonDecreasing(a: List[int]) -> bool:
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            return False
    return True


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        arr = nums[:]
        ans = 0
        while not isNonDecreasing(arr):
            k = 0
            s = arr[0] + arr[1]
            for i in range(1, len(arr) - 1):
                t = arr[i] + arr[i + 1]
                if s > t:
                    s = t
                    k = i
            arr[k] = s
            arr.pop(k + 1)
            ans += 1
        return ans
