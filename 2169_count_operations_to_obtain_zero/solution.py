# LeetCode 2169 - Count Operations to Obtain Zero
# https://leetcode.com/problems/count-operations-to-obtain-zero/
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                ans += num1 // num2
                num1 %= num2
            else:
                ans += num2 // num1
                num2 %= num1
        return ans
