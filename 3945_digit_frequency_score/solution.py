# LeetCode 3945 - Digit Frequency Score
# https://leetcode.com/problems/digit-frequency-score/


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += n % 10
            n //= 10
        return ans
