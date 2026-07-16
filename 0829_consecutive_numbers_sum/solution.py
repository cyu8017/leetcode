# LeetCode 0829 - Consecutive Numbers Sum
# https://leetcode.com/problems/consecutive-numbers-sum/

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # n = k*a + k*(k-1)/2  =>  (n - k*(k-1)/2) % k == 0, a >= 1
        ans = 0
        k = 1
        while k * (k - 1) // 2 < n:
            if (n - k * (k - 1) // 2) % k == 0:
                ans += 1
            k += 1
        return ans
