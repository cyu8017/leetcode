# LeetCode 0989 - Add to Array-Form of Integer
# https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        i = len(num) - 1
        while k or i >= 0:
            if i >= 0:
                k += num[i]
                num[i] = k % 10
                i -= 1
            else:
                num.insert(0, k % 10)
            k //= 10
        return num
