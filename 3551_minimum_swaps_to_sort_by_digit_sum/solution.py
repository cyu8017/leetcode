# LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
# https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

from typing import List


def f3551(x: int) -> int:
    s = 0
    while x != 0:
        s += x % 10
        x //= 10
    return s


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [[f3551(nums[i]), nums[i]] for i in range(n)]
        arr.sort(key=lambda x: (x[0], x[1]))
        d = {arr[i][1]: i for i in range(n)}
        vis = [False] * n
        ans = n
        for i in range(n):
            if not vis[i]:
                ans -= 1
                j = i
                while not vis[j]:
                    vis[j] = True
                    j = d[nums[j]]
        return ans
