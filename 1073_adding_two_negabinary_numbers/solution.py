# LeetCode 1073 - Adding Two Negabinary Numbers
# https://leetcode.com/problems/adding-two-negabinary-numbers/

class Solution:
    def addNegabinary(self, arr1: list[int], arr2: list[int]) -> list[int]:
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        ans: list[int] = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += arr1[i]
                i -= 1
            if j >= 0:
                total += arr2[j]
                j -= 1
            ans.append(total & 1)
            carry = -(total >> 1)
        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()
        return ans[::-1]
