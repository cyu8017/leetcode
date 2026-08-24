# LeetCode 2191 - Sort the Jumbled Numbers
# https://leetcode.com/problems/sort-the-jumbled-numbers/

from typing import List
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapVal(x):
            if x == 0:
                return mapping[0]
            digits = []
            while x > 0:
                digits.append(x % 10)
                x = x // 10
            res = 0
            for i in range(len(digits) - 1, (0) - 1, -1):
                res = res * 10 + mapping[digits[i]]
            return res

        n = len(nums)
        arr = [[mapVal(nums[i]), i, nums[i]] for i in range(n)]
        arr.sort(key=lambda x: (x[0], x[1]))
        return [x[2] for x in arr]
