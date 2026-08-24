# LeetCode 2164 - Sort Even and Odd Indices Independently
# https://leetcode.com/problems/sort-even-and-odd-indices-independently/

from typing import List
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        ei = 0
        oi = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even[ei]
                ei += 1
            else:
                nums[i] = odd[oi]
                oi += 1
        return nums
