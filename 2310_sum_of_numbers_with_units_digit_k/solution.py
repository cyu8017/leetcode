# LeetCode 2310 - Sum of Numbers With Units Digit K
# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/


class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        for count in range(1, 11):
            if count * k % 10 == num % 10 and count * k <= num:
                return count
        return -1
