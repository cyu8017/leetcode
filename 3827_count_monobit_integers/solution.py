# LeetCode 3827 - Count Monobit Integers
# https://leetcode.com/problems/count-monobit-integers/

class Solution:
    def countMonobit(self, n: int) -> int:
        ans = 1
        i = 1
        x = 1
        while x <= n:
            ans += 1
            x += 1 << i
            i += 1
        return ans
