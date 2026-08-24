# LeetCode 3723 - Maximize Sum of Squares of Digits
# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/


class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num * 9 < sum:
            return ""
        k, rem = divmod(sum, 9)
        ans = "9" * k
        if rem > 0:
            ans += chr(48 + rem)
        while len(ans) < num:
            ans += "0"
        return ans
