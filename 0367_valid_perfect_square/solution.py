# LeetCode 0367 - Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            if square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
